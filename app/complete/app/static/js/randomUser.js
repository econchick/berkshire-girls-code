var fillRandomUser = (function() {
    function getRandomUser(form) {
        var popularUsers = Array("spotify_germany", "magerleagues", "spotify", "mobymus", "sonymusicuk", "warnermusicus");
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
