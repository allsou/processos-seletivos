using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace GSWAvaliacao.Models
{
    public class ListaFornecedores
    {
        public List<FornecedorModel> fornecedores { get; set; }

        public ListaFornecedores()
        {
            List<FornecedorModel> forn = new List<FornecedorModel>();
            var empresas = new ListaEmpresas().empresas;
            Random aleatorio = new Random();

            var fornecedores = new List<FornecedorModel>();
            forn.Add(
                new FornecedorEmpresaModel(
                    empresas[aleatorio.Next(empresas.Count)],
                    "Oliver e Fátima Esportes Ltda",
                    "14.270.957/0001-62",
                    new DateTime(2009, 5, 13),
                    new List<String>() { "(85) 98238-4895", "(85) 98238-4895", "(85) 98238-4895" }));
            forn.Add(
                new FornecedorPessoaFisicaModel(
                    empresas[aleatorio.Next(empresas.Count)],
                    "Enrico Cauã Calebe Barbosa",
                    new DateTime(2009, 5, 11),
                    new List<String>() { "(85) 3865-6362", "(85) 98238-4895" },
                    "111.058.338-95",
                    "24.696.413-3",
                    new DateTime(1954, 7, 22)));

            this.fornecedores = forn;
        }
    }
}
