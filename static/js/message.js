/**
 * Created by eleven on 15-11-26.
 */
$(document).on("mouseover", "#nav-message-wrap #message-icon", function(event){
    console.log("fuck");
    if(!$("#nav-message-wrap #message-dropdown").html().trim()) {
        $.get("/a/message/list", function(data) {
            var html = "";
            data = data["result"]
            for(var i= 0; i < data.length; i++) {
                html += "<li>" + data[i]["comment_nickname"] + " 回复了你: " + data[i]["content"] + "</li>"
            }
            $("#nav-message-wrap #message-dropdown").html(html);
            $(".has-message").removeClass("has-message");
        })
    }
});