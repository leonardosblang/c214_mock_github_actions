import mock
import softest
import io
from professor import Professor
import xmlrunner
from xmlrunner.extra.xunit_plugin import transform
# objeto mock criado usando como referencia a classe Professor
mock_professor = mock.Mock(spec=Professor)


# testes unitarios usando o objeto mock
class testeProfessor(softest.TestCase):
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
        self.soft_assert(self.assertNotEqual, mock_professor.change_horario_de_atendimento(), "Segunda 17:00",
                         "Horario diferente")

        self.assert_all()

    def test_Periodo_fail(self):
        mock_professor.change_periodo.return_value = "Noturno"
        self.soft_assert(self.assertNotEqual, mock_professor.change_periodo(), "Integral", "Periodo diferente")

        self.assert_all()

    def test_Salario_fail(self):
        mock_professor.salario.return_value = 100
        self.soft_assert(self.assertNotEqual, mock_professor.salario(), 200, "Salario diferente")

        self.assert_all()


if __name__ == '__main__':
    softest.main()
    out = io.BytesIO()
    softest.main(
        testRunner=xmlrunner.XMLTestRunner(output=out),
        failfast=False, buffer=False, catchbreak=False, exit=False
    )
    with open("unit-test.xml", "wb") as report:
        report.write(transform(out.getvalue()))
