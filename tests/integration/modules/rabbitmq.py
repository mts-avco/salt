import os

# Import salt libs
try:
    import integration
except ImportError:
    if __name__ == '__main__':
        import sys
        sys.path.insert(
            0, os.path.abspath(
                os.path.join(
                    os.path.dirname(__file__), '../../'
                )
            )
        )
    import integration


class RabbitModuleTest(integration.ModuleCase):
    '''
    Validates the rabbitmqctl functions.
    To run these tests, you will need to be able to access the rabbitmqctl
    commands.
    '''
    def setUp(self):
        super(RabbitModuleTest, self).setUp()
        ret = self.run_function('cmd.has_exec', ['rabbitmqctl'])
        if not ret:
            self.skipTest('RabbitMQ not installed')
        if os.geteuid() != 0:
            self.skipTest('You must be root to run this test')

    def test_user_exists(self):
        '''
        Find out whether a user exists.
        '''
        ret = self.run_function('rabbitmq.user_exists', ['null_user'])
        self.assertEqual(ret, False)


if __name__ == '__main__':
    from integration import run_tests
    run_tests(RabbitModuleTest)
