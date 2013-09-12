var initConnections = function() {
    // Get pagename
    var path = window.location.pathname;
    var pagename = path.substring(path.lastIndexOf("/") + 1)
    pagename = pagename.toLowerCase();

    // Add Autocomplete to connections search box
    $('#connectionSearchBox').autocomplete({
        source: "/get/pages/",
        minLength: 1,
        focus: function (event, ui) {
            $("#connectionSearchBox").val(ui.item['name']);
            $("#connectionSearchBox")[0].setAttribute('data-vanity-url', ui.item['vanity']);
            return false;
        },
        select: function (event, ui) {
            //redirect to content page for that entry
            $("#connectionSearchBox").val(ui.item['name']);
            $("#connectionSearchBox")[0].setAttribute('data-vanity-url', ui.item['vanity']);
            return false;
        }
    }).data("autocomplete")._renderItem = function (ul, item) {
        var re = new RegExp(this.term, "i");
        var match = item.name.match(re);
        var t = item['name'].replace(re, "<span class='autocomplete-name-term-highlight'>" +
            match +
            "</span>");

        var innerContent = "<a><span class='autocomplete-name'>" + t + "</span><span class='autocomplete-category-box " + item['type'] + "'></span>";

        if (pagename === "") {
            innerContent += "<span class='autocomplete-category " + item['type'] + "'>" + item['type'].toUpperCase() + "</span>";
        }

        innerContent += "</a>";

        return $("<li></li>")
            .data("item.autocomplete", item)
            .append(innerContent)
            .appendTo(ul);
    };
}

$(document).ready(function () {
    if ($('#connectionSearchBox').length != 0) {
        initConnections();
    }
});
