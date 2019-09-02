using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Dynamic;
using System.Linq;
using System.Threading.Tasks;
using GSWAvaliacao.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;


namespace GSWAvaliacao.Controllers
{
    public class FornecedorController : Controller
    {

        public IActionResult Cadastro([FromServices] List<EmpresaModel> empresas)
        {
            FornecedorCadastroModel fornecedorView = new FornecedorCadastroModel();
            fornecedorView.empresas = empresas;
            /*dynamic modelos = new ExpandoObject();
            modelos.Empresas = empresas;
            modelos.Fornecedor = new FornecedorModel();*/
            return View(fornecedorView);
        }

        public IActionResult Lista([FromServices] List<FornecedorModel> fornecedores)
        {
            return View(fornecedores);
        }

        public IActionResult Editar([FromServices] List<FornecedorModel> fornecedores)
        {
            return View(fornecedores);
        }

        public IActionResult Edicao(string Nome, [FromServices] List<FornecedorModel> fornecedores, [FromServices] List<EmpresaModel> empresas)
        {
            foreach (object forn in fornecedores)
            {
                //Debug.WriteLine(forn.GetType());
                //GSWAvaliacao.Models.FornecedorEmpresaModel
                FornecedorModel f = (FornecedorModel)forn;
                Debug.WriteLine(f.Nome);
                if (f.Nome.Equals(Nome))
                {
                    if (forn.GetType().ToString().Equals("GSWAvaliacao.Models.FornecedorEmpresaModel"))
                    {
                        FornecedorCadastroModel toView = new FornecedorCadastroModel();
                        toView.empresas = empresas;
                        toView.fornecedorEmp = (FornecedorEmpresaModel)forn;
                        return View("Edicao", toView);
                    }
                    else
                    {
                        FornecedorCadastroModel toView = new FornecedorCadastroModel();
                        toView.empresas = empresas;
                        toView.fornecedorPes = (FornecedorPessoaFisicaModel)forn;
                        return View("Edicao", toView);
                    }
                }
                
            }
            return View();
        }

        public IActionResult Cadastrar(IFormCollection form, [FromServices] List<FornecedorModel> fornecedores, [FromServices] List<EmpresaModel> empresas)
        {
            //form["fornecedor.Telefones"]
            List<String> teles = new List<string>();
            var cont = 0;
            while (!form["fornecedor.Telefones[" + cont + "]"].ToString().Equals(""))
            {
                teles.Add(form["fornecedor.Telefones[" + cont + "]"]);
                cont++;
            }
            EmpresaModel empForn = null;
            foreach(EmpresaModel emp in empresas)
            {
                if(form["fornecedor.Empresa.NomeFantasia"].Equals(emp.NomeFantasia))
                {
                    empForn = new EmpresaModel(emp.NomeFantasia,emp.UF,emp.CNPJ);
                    break;
                }
            }
            //form["fornecedorPes.DataNascimento"]
            if (form["tipoDoc"].Equals("cpf"))
            {
                FornecedorPessoaFisicaModel fornecedorPessoa = new FornecedorPessoaFisicaModel(
                    empForn,
                    form["fornecedor.Nome"],
                    DateTime.Now,
                    teles,
                    form["fornecedor.Documento"],
                    form["fornecedorPes.RG"],
                    DateTime.Parse(form["fornecedorPes.DataNascimento"])
                    );
                if(fornecedorPessoa.validate())
                {
                    fornecedores.Add(fornecedorPessoa);
                }
                    
            }
            else
            {
                FornecedorEmpresaModel fornecedorEmpresa = new FornecedorEmpresaModel(
                    empForn,
                    form["fornecedor.Nome"],
                    form["fornecedor.Documento"],
                    DateTime.Now,
                    teles
                    );
                fornecedores.Add(fornecedorEmpresa);
            }

            
            return View("Lista",fornecedores);
        }

        public IActionResult EX(IFormCollection form, [FromServices] List<FornecedorModel> fornecedores)
        {
            int cont = 0;
            foreach(FornecedorModel fornecedor in fornecedores)
            {
                if (form.ContainsKey("fornecedorEmp.Nome"))
                {
                    if (form["fornecedorEmp.Nome"].Equals(fornecedor.Nome))
                    {
                        fornecedores.RemoveAt(cont);
                        break;
                    }
                }
                else
                {
                    if (form["fornecedorPes.Nome"].Equals(fornecedor.Nome))
                    {
                        fornecedores.RemoveAt(cont);
                        break;
                    }
                }
                cont++;
            }
            return View("Lista", fornecedores);
        }
        public IActionResult ED(IFormCollection form, [FromServices] List<FornecedorModel> fornecedores, [FromServices] List<EmpresaModel> empresas)
        {
            int idForn = 0;
            foreach (FornecedorModel fornecedor in fornecedores)
            {
                if (form.ContainsKey("fornecedorEmp.Nome"))
                {
                    if (form["fornecedorEmp.Nome"].Equals(fornecedor.Nome))
                    {
                        EmpresaModel emp = new EmpresaModel("", "", "");
                        foreach (EmpresaModel empresa in empresas)
                        {
                            if (form["fornecedorEmp.Empresa.NomeFantasia"].Equals(empresa.NomeFantasia))
                            {
                                emp = empresa;
                                break;
                            }
                        }
                        List<String> teles = new List<string>();
                        var cont = 0;
                        while (!form["fornecedor.Telefones[" + cont + "]"].ToString().Equals(""))
                        {
                            teles.Add(form["fornecedor.Telefones[" + cont + "]"]);
                            cont++;
                        }
                        
                        fornecedores.RemoveAt(idForn);
                        fornecedores.Add(new FornecedorEmpresaModel(
                            emp,
                            form["fornecedorEmp.Nome"],
                            form["fornecedorEmp.Documento"],
                            DateTime.Now,
                            teles));
                        break;
                    }
                }
                else
                {
                    if (form["fornecedorPes.Nome"].Equals(fornecedor.Nome))
                    {
                        EmpresaModel emp = new EmpresaModel("", "", "");
                        foreach (EmpresaModel empresa in empresas)
                        {
                            if (form["fornecedorPes.Empresa.NomeFantasia"].Equals(empresa.NomeFantasia))
                            {
                                emp = empresa;
                                break;
                            }
                        }
                        List<String> teles = new List<string>();
                        var cont = 0;
                        while (!form["fornecedor.Telefones[" + cont + "]"].ToString().Equals(""))
                        {
                            teles.Add(form["fornecedor.Telefones[" + cont + "]"]);
                            cont++;
                        }
                        FornecedorPessoaFisicaModel forne = new FornecedorPessoaFisicaModel(
                            emp,
                            form["fornecedorPes.Empresa.NomeFantasia"],
                            DateTime.Now,
                            teles,
                            form["fornecedorPes.Documento"],
                            form["fornecedorPes.RG"],
                            DateTime.Parse("fornecedorPes.DataNascimento"));
                        if(forne.validate())
                        {
                            fornecedores.RemoveAt(idForn);
                            fornecedores.Add(forne);
                        }
                        break;
                        /*fornecedor = new FornecedorPessoaFisicaModel(
                            )*/
                        /*fornecedorPes.Empresa.NomeFantasia: Consultoria Financeira Ltda
                        fornecedorPes.Nome: Enrico Cauã Calebe Barbosa
                        fornecedorPes.Documento: 111.058.338 - 95
                        fornecedorPes.RG: 24.696.413 - 3
                        fornecedorPes.DataNascimento: 
                        fornecedorPes.Telefones[0]: (85) 3865 - 6362
                        fornecedorPes.Telefones[1]: (85) 98238 - 4895*/
                    }
                }
                idForn++;
            }
            return View("Lista", fornecedores);
        }
    }
}