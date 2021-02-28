$(window).load(function() {
    showDropdown();
});

function showDropdown() {
    $(".te_custom_submenu").parent("li.nav-item").addClass("dropdown");
    $(".te_custom_submenu").siblings("a.nav-link").addClass("dropdown-toggle").attr("data-toggle", "dropdown");
    $(".static_menu").parent("li.nav-item").css("position", "static");
}

if ($(window).innerWidth() > 1200) {
    $("#top_menu > .dropdown").each(function() {
        if (!$(this).closest(".o_extra_menu_items").length) {
            $(this).closest("a").click(function() {
                return false;
            });
            $(this).hover(
                function() {
                    $('> .dropdown-menu', this).stop(true, true).fadeIn("slow");
                    $(this).toggleClass('open');
                },
                function() {
                    $('> .dropdown-menu', this).stop(true, true).fadeOut("fast");
                    $(this).toggleClass('open');
                }
            );
        }
        //extra menu dropdown
        $('.o_extra_menu_items .dropdown-menu').css("display", "none")
        $('li.o_extra_menu_items .dropdown').click(function(event) {
            event.stopImmediatePropagation();
            $(this).find(".dropdown-menu").slideToggle();
        });
    })
}
