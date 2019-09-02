using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class FornecedorCadastroModel : FornecedorModel
    {
        public List<EmpresaModel> empresas { get; set; }
        public FornecedorModel fornecedor { get; set; }
        public FornecedorEmpresaModel fornecedorEmp { get; set; }
        public FornecedorPessoaFisicaModel fornecedorPes{ get; set; }
    }
}
