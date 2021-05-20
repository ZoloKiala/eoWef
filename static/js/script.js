$(document).ready(function(){
    $('#table').DataTable({
        "order": [[ 0, "desc" ]],
        'iDisplayLength':25
    });
    
    $('[data-toggle="tooltip"]').tooltip();



});

