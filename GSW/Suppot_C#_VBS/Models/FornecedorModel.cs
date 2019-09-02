using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class FornecedorModel
    {
        public EmpresaModel Empresa { get; set; }
        public String Nome { get; set; }
        public DateTime Cadastro { get; set; }
        public List<String> Telefones { get; set; }
        public String Documento { get; set; }

        public string telefonesString()
        {
            string retorno = "";
            foreach(var telefone in this.Telefones)
            {
                retorno += telefone + " | ";
            }
            return retorno;
        }
    }
}
