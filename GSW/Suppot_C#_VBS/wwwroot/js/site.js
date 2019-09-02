// Please see documentation at https://docs.microsoft.com/aspnet/core/client-side/bundling-and-minification
// for details on configuring this project to bundle and minify static web assets.

// Write your JavaScript code.

$(document).ready(function () {
    cont = 1
    $('#cnpj').mask('00.000.000/0000-00', { reverse: false });
    $('#cpf').mask('000.000.000-00', { reverse: false });
    $('.docs').mask('000.000.000-00', { reverse: false });
    $('#rg').mask('00.000.000-0', { reverse: false });
    $('#tel').mask('(00) 0000-0000');
    $('#tabela').DataTable({
        "language": {
            "search": "Pesquisar:",
            "lengthMenu": "",
            "emptyTable": "Sem registros...",
            "info": "Mostrando de _START_ a _END_ de _TOTAL_ registros",
            "infoFiltered": "(filtrados de _MAX_ registros)",
            "zeroRecords": "Nenhum registro corresponde ao filtro...",
            "paginate": {
                "next": "Próximo",
                "previous": "Anterior"
            }
        }
    });
    $('#tipoDocP').click(function () {
        $('.docs').mask('000.000.000-00', { reverse: false });
        $('#rg').prop('disabled', false);
        $('#datanascimento').prop('disabled', false);
    });
    $('#tipoDocJ').click(function () {
        $('.docs').mask('00.000.000/0000-00', { reverse: false });
        $('#rg').prop('disabled', true);
        $('#datanascimento').prop('disabled', true);
    }); 
    $('#addTel').click(function () {
        //str = '<input type="text" class="form-control" asp-for="fornecedor.Telefones[' + cont + ']" id="tel' + cont + '" placeholder="Telefone">';
        str = '<input type="text" class="form-control" id="tel' + cont + '" placeholder="Telefone" name="fornecedor.Telefones[' + cont + ']" value="" maxlength="14">';
        //input = jQuery('<input type="text" class="form-control" asp-for="fornecedor.Telefones" id="tel" placeholder="Telefone">');
        input = jQuery(str);
        jQuery('#tels').append(input);
        $('#tel'+cont).mask('(00) 0000-0000');
        cont++;
    });
});

