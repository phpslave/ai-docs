import unittest
from click.testing import CliRunner
from ai_docs.cli import cli

class TestCLI(unittest.TestCase):
    def test_collect_command(self):
        runner = CliRunner()
        result = runner.invoke(cli, ['collect', 'https://example.com', 'output.md'])
        self.assertEqual(result.exit_code, 0)

if __name__ == '__main__':
    unittest.main()