    $(document).ready(function() {
        $('.datepicker').datepicker();
    });


/*$(document).ready(function(){

    $('#id_application_method').on('change', function() {

        $('.method_options').hide();
        $('#tr_' + $(this).val() ).show();

    });

}); */

$(document).ready(function(){

    $('#id_application_method').on('change', function() {

        $('.other_option').hide();
        $('#' + $(this).val() ).show();

    });

});
