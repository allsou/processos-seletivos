import React, { Component } from 'react'

class Header extends Component{
    render(){
        return(
            <nav class="navbar navbar-fixed-top">
            <div class="container">
                    <div class="navbar-collapse collapse">
                        <ul class="nav navbar-nav">
                            <li>
                                <a asp-area="" asp-controller="Fornecedor" asp-action="" class="dropdown-toggle" data-toggle="dropdown">Fornecedor<span class="caret"></span></a>
                                <ul class="dropdown-menu">
                                    <li><a asp-area="" asp-controller="Fornecedor" asp-action="Lista">Listar</a></li>
                                    <li><a asp-area="" asp-controller="Fornecedor" asp-action="Cadastro">Cadastrar</a></li>
                                    <li><a asp-area="" asp-controller="Fornecedor" asp-action="Editar">Editar</a></li>
                                </ul>
                            </li>
                            <li>
                                <a asp-area="" asp-controller="Empresa" asp-action="" class="dropdown-toggle" data-toggle="dropdown">Empresa<span class="caret"></span></a>
                                <ul class="dropdown-menu">
                                    <li><a asp-area="" asp-controller="Empresa" asp-action="Lista">Listar</a></li>
                                    <li><a asp-area="" asp-controller="Empresa" asp-action="Cadastro">Cadastrar</a></li>
                                    <li><a asp-area="" asp-controller="Empresa" asp-action="Editar">Editar</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        )
    }
}

export default Header