using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class EmpresaModel
    {
        public EmpresaModel(string nomeFantasia, string uF, string cNPJ)
        {
            NomeFantasia = nomeFantasia;
            UF = uF;
            CNPJ = cNPJ;
        }

        public String NomeFantasia { get; set; }
        public String UF { get; set; }
        public String CNPJ { get; set; }
    }
}