var fillRandomUser = (function() {
    function getRandomUser(form) {
        var popularUsers = Array("econchick", "sp-10");
        var item = popularUsers[Math.floor(Math.random()*popularUsers.length)];
        $(form).find(".sp-user").each(function(index, el){
            var $el = $(el),
                id = $el.attr("id"),
                name = $el.attr("name"),
                value;

            $el.val(item);
        })
    }
    function fillRandomUser() {
        var form = $("form#sp-user");
        getRandomUser(form);
    }
    return fillRandomUser
 })();
