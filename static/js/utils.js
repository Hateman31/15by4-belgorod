$("button").click(function(){
    $.ajax({url: "/demo", success: function(result){
        $("#div1").html(result);
    }});
});
