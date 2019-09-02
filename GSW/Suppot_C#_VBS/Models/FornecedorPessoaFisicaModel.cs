using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class FornecedorPessoaFisicaModel : FornecedorModel
    {
        public FornecedorPessoaFisicaModel(
            EmpresaModel empresa,
            string nome,
            DateTime cadastro,
            List<String> telefones,
            string cpf,
            string rg,
            DateTime dataNascimento)
        {
            Empresa = empresa;
            Nome = nome;
            Cadastro = cadastro;
            Telefones = telefones;
            Documento = cpf;
            RG = rg;
            DataNascimento = dataNascimento;
        }

        public String CPF { get; set; }
        public String RG { get; set; }
        public DateTime DataNascimento { get; set; }

        public bool validate()
        {
            bool retorno = true;
            if (Empresa.UF.Equals("PR") && (DateTime.Now.Year - DataNascimento.Year < 18))
            {
                retorno = false;
            }
            return retorno;
        }
    }
}
