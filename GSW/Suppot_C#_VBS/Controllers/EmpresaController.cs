using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Linq;
using System.Threading.Tasks;
using GSWAvaliacao.Models;
using Microsoft.AspNetCore.Mvc;

namespace GSWAvaliacao.Controllers
{
    public class EmpresaController : Controller
    {
        public IActionResult Cadastro()
        {
            return View();
        }

        public IActionResult Lista([FromServices] List<EmpresaModel> empresas)
        {
            return View(empresas);
        }

        public IActionResult Cadastrar(string NomeFantasia, String UF, string CNPJ, [FromServices] List<EmpresaModel> empresas)
        {
            EmpresaModel novaEmpresa = new EmpresaModel(NomeFantasia, UF, CNPJ);
            empresas.Add(novaEmpresa);
            return View("Lista", empresas);
        }

        public IActionResult Editar([FromServices] List<EmpresaModel> empresas)
        {
            dynamic modelos = new ExpandoObject();
            modelos.Empresas = empresas;
            modelos.Empresa = new EmpresaModel("","","");
            return View(modelos);
        }
        public IActionResult Edicao(string NomeFantasia, [FromServices] List<EmpresaModel> empresas)
        {
            foreach(EmpresaModel empresa in empresas)
            {
                if (empresa.NomeFantasia.Equals(NomeFantasia))
                {
                    return View(empresa);
                }
            }
            return View();
        }
        public IActionResult ED(string UF , string NomeFantasia, string CNPJ, [FromServices] List<EmpresaModel> empresas)
        {
            foreach (EmpresaModel empresa in empresas)
            {
                if (empresa.NomeFantasia.Equals(NomeFantasia))
                {
                    empresa.CNPJ = CNPJ;
                    empresa.UF = UF;
                    return View("Lista",empresas);
                }
            }
            return View();
        }
        public IActionResult EX(string UF, string NomeFantasia, string CNPJ, [FromServices] List<EmpresaModel> empresas)
        {
            int cont = 0;
            foreach (EmpresaModel empresa in empresas)
            {
                if (empresa.NomeFantasia.Equals(NomeFantasia))
                {
                    break;
                }
                cont++;
            }
            empresas.RemoveAt(cont);
            return View("Lista", empresas);
        }
    }
}