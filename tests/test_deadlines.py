from deadlines.models import Schedule


class TestDeadlineDocument(object):

    def test_parse(self):
        doc = {
            'schedule': 'daily',
            'targets': 'http://foo.com/path/to/result.csv'
        }

        result = Schedule.from_doc(doc)

        assert result.scope == 'daily'
