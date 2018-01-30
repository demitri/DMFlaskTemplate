$(function () {
    $("#menu").metisMenu();
    function setFrameSizes() {
        console.log("Set scrollbar");
        $('.content-scroll').slimScroll({
            height: $(window).height() - 20,
            size: '4px',
            color: '#ddd'
        });
    };
    $(document).ready(function () {
        setFrameSizes();
    });
    $(window).resize(function () {
        setFrameSizes();
    });
    $(".sidebar-toggler").click(function(){
    $(".page-wrapper").toggleClass("sidebar-enable");
});
 $('[data-toggle="tooltip"]').tooltip();
 $('[data-toggle="popover"]').popover();
 $('[data-original-title=""]').tooltip();
});
