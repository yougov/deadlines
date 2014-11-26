"""Tasks provide tools to create targets. Targets are the result we
want. A target is a class that implements two methods, `to_uri` and
`exists`.

The `to_uri` method provides a means of comparing targets. For
example, a S3 Target might provide the following URI:

  s3target://my-bucket/path/to/file.csv.gz

If the target were a database table the URI might look like:

  postgres://dbhost:port/database/tablename

The target can use these details to create a valid and appropriately
unique URI.
"""

from pkg_resources import iter_entry_points
from urlparse import urlparse

from cytoolz.itertoolz import merge_sorted, isiterable


def target_classes():
    for ep in merge_sorted(iter_entry_points('deadlines.targets')):
        yield ep


def target_class(name):
    for entry_point in target_classes():
        if entry_point.name == name:
            return entry_point.load()


def tasks():
    for ep in merge_sorted(iter_entry_points('deadlines.tasks')):
        yield ep.load()


def available_targets():
    for task in tasks():
        task = task()
        targets = task.output()
        if isiterable(targets):
            for target in targets:
                yield target
        else:
            yield targets


def uri_to_target(uri):
    parts = urlparse(uri)
    cls = target_class(parts.scheme)
    return cls(uri)


def find_target(uri):
    for target in available_targets():
        if target.to_uri() == uri:
            return target


if __name__ == '__main__':
    print(list(available_targets()))
    print(uri_to_target('foofile://foo.txt'))
    print(find_target('foofile://foo.txt'))
