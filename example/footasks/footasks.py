import luigi
import arrow


class FooFile(luigi.LocalTarget):

    def to_uri(self):
        return 'foofile://%s' % self.path


class Bar(luigi.Task):

    def output(self):
        return luigi.LocalTarget('bar.txt')

    def run(self):
        with self.output('w') as out:
            for i in range(100):
                out.write(str(i) + '\n')


class Foo(luigi.Task):

    def requires(self):
        return Bar()

    def output(self):
        return FooFile('foo.txt')

    def run(self):
        total = sum(1 for line in self.input('r').open())
        out = self.output('w').open()
        out.write('Total: %s' % total)
        out.close()


class FooPlanner(luigi.Task):

    start = luigi.DateParameter()
    end = luigi.DateParameter()

    def spec(self):
        """Return the Task to run along with the specific arguments."""
        return [
            {'task': 'foo', 'kwargs': {'day': day}}
            for day in arrow.Arrow.range('day', self.start, self.end)
        ]
