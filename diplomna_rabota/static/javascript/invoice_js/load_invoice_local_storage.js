$(document).ready(function() {
    // dds
    if (localStorage.getItem('id_dds')) {
        $('#id_DDS').val(localStorage.getItem('id_dds'))
    }
    $('#id_DDS').on('change', function () {
        localStorage.setItem('id_dds', $(this).val())
    })

    // comment
    if (localStorage.getItem('id_comment')) {
        $('#id_comment').val(localStorage.getItem('id_comment'))
    }
    $('#id_comment').on('input', function () {
        localStorage.setItem('id_comment', $(this).val())
    })

    //discount
    if (localStorage.getItem('id_discount')) {
        $('#id_discount').val(localStorage.getItem('id_discount'))
    }
    $('#id_discount').on('input', function () {
        localStorage.setItem('id_discount', $(this).val())
    })

    // company
    if (localStorage.getItem('id_company')) {
        $('#id_company').val(localStorage.getItem('id_company')).trigger('change')
    }
    $('#id_company').on('change', function () {
        localStorage.setItem('id_company', $(this).val())
    })

    // order
    if (localStorage.getItem('id_order')) {
        $('#id_order').val(localStorage.getItem('id_order')).trigger('change')
    }
    $('#id_order').on('change', function () {
        localStorage.setItem('id_order', $(this).val())
    })

    $('#cancel_btn').on('click', function () {
        localStorage.clear()
    })

    $('#submit_btn').on('click', function () {
        localStorage.clear()
    })
})