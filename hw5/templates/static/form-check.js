$( document ).ready(function() {
    $("#reg_form").bind("submit", function( event ) {
        event.preventDefault();
        data = $( this ).serialize();
        $.post("/form", data, function( result ) {
            var form = $('#reg_form');
            if (result['success'] == true) {
                
                form.hide();

                if ($("h1")) {
                    $("h1").hide();
                    $(".alert").hide();
                }

                form.before('<h1 style="color: green;">Ура, получилось!</h1>');
                
                html = "<ul>";
                for (key in result) {
                    if (key !== 'success') {
                        html += "<li><strong>" + key + "</strong>:&nbsp;" + result[key] + "</li>";
                    }
                }
                html += "</ul>";

                form.before(html);
            } else {
                form.before('<div class="alert alert-danger" role="alert">Заполните форму полностью!</div>');
            }
        });
    });

    $(".form-control").bind("change", function( event ) {
        data = {}
        data['value'] = $(this).val();
        data['name'] = $(this).attr("name");
        
        $.getJSON( "/check/", data, function( json ) {
            if(json['status'] == 'success') {
                var el = $("#id_" + json['name']).closest("div");
                el.css("border-bottom", "4px solid green");
            }
        });
    });
});