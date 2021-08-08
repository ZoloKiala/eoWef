$(document).ready(function() {
    $('#sidebarCollapse').on('click', function() {
      $('#sidebar, #content').toggleClass('active');
      $('.collapse.in').toggleClass('in');
      $('a[aria-expanded=true]').attr('aria-expanded', 'true');
      document.getElementById("content").style.width="100%";
    });

    $('#table').DataTable({
      "order": [[ 0, "desc" ]],
      'iDisplayLength':25
  });
  
  $('[data-toggle="tooltip"]').tooltip();


});