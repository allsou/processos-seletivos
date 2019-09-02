using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class ListaEmpresas
    {

        public List<EmpresaModel> empresas { get; set; }
        public ListaEmpresas()
        {
            List<EmpresaModel> emp = new List<EmpresaModel>();
            emp.Add(new EmpresaModel("Consultoria Financeira Ltda", "SP", "62.292.363/0001-03"));
            emp.Add(new EmpresaModel("Raul Ferragens ME", "BA", "83.417.503/0001-94"));
            emp.Add(new EmpresaModel("Heitor Marketing Ltda", "MA", "87.027.391/0001-16"));
            emp.Add(new EmpresaModel("Eletrônica Ltda", "RR", "43.069.096/0001-57"));
            emp.Add(new EmpresaModel("Locações de Automóveis Ltda", "TO", "09.615.104/0001-85"));
            this.empresas = emp;
        }

    }
}
