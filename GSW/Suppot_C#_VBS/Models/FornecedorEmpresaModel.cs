using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class FornecedorEmpresaModel : FornecedorModel
    {
        public FornecedorEmpresaModel(
            EmpresaModel empresa,
            string nome,
            string cnpj,
            DateTime cadastro,
            List<String> telefones
            )
        {
            Empresa = empresa;
            Nome = nome;
            Documento = cnpj;
            Cadastro = cadastro;
            Telefones = telefones;
        }

        public String CNPJ { get; set; }
    }
}
