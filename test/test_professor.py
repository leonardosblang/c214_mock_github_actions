import mock
import unittest
import io
from professor import Professor
import xmlrunner
from xmlrunner.extra.xunit_plugin import transform
# objeto mock criado usando como referencia a classe Professor
mock_professor = mock.Mock(spec=Professor)


# testes unitarios usando o objeto mock
class testeProfessor(unittest.TestCase):
    def test_Atendimento(self):
        mock_professor.change_horario_de_atendimento.return_value = "Segunda 17:30"
        self.assertEqual(mock_professor.change_horario_de_atendimento(), "Segunda 17:30")

    def test_Periodo(self):
        mock_professor.change_periodo.return_value = "Noturno"
        self.assertEqual(mock_professor.change_periodo(), "Noturno")

    def test_Salario(self):
        mock_professor.salario.return_value = 100
        self.assertEqual(mock_professor.salario(), 100)

    def test_Atendimento_fail(self):
        mock_professor.change_horario_de_atendimento.return_value = "Segunda 17:30"
        self.assertNotEqual(mock_professor.change_horario_de_atendimento, "Segunda 17:00")




if __name__ == '__main__.py':
    print("Testes unitarios usando mock")
    out = io.BytesIO()
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output=out),
        failfast=False, buffer=False, catchbreak=False, exit=False
    )
    print("Testes unitarios usando mock 2")
    with open("TEST-report.xml", "wb") as report:
        report.write(transform(out.getvalue()))