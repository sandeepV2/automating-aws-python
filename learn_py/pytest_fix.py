import pytest

class Testclass:
    @pytest.fixture(autouse=True)
    def setup_fixture(self, request):
        print 'setup fixture'
        def teardown():
            print 'teardown fixture'
        request.addfinalizer(teardown)

    def setup_class(self):
        print 'Setting up class'

    def teardown_class(self):
        print 'Teardown the class'

    def setup_method(self):
        print 'setting up method'

    def teardown_method(self):
        print 'clean up method'

    def test_assert(self):
        assert True

