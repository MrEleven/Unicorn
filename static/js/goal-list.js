/**
 * Created by eleven on 15-10-22.
 */
function click_scroll(obj_id) {
    var scroll_offset = $(obj_id).offset();
    $("body").animate({
        scrollTop: scroll_offset.top-15
    }, 250);
}
$(function () {
    $("#goal-nav ul a").click(function () {
        var goal_id = $(this).attr("goal-id");
        var target_id = "#goal-" + goal_id;
        click_scroll(target_id);
    });
    $("#goal-edit-cancel-btn").click(function () {
        $("#goal-edit-wrap .name-input").val("");
        $("#goal-edit-wrap .desc-input").val("");
        //$("#goal-edit-wrap .album").attr("src", "");
        $("#goal-edit-modal").removeClass("modal");
        $("#goal-edit-modal").addClass("empty");
    });
    $("#goal-add-cancel-btn").on("click", function () {
        $("#goal-add-wrap .name-input").val("");
        $("#goal-add-wrap .desc-input").val("");
        //$("#goal-add-wrap .album").attr("src", "");
        $("#goal-add-modal").removeClass("modal");
        $("#goal-add-modal").addClass("empty");
    });
    $("#todo-edit-cancel-btn").on("click", function () {
        $("#goal-add-wrap .name-input").val("");
        $("#goal-add-wrap .note-input").val("");
        $("#todo-edit-modal").removeClass("modal").addClass("empty");
    });
    $("#goal-list-wrap #goal-list-ul .goal-wrap").hover(function() {
        $(this).children(".ops").show();
    }, function() {
        $(this).children(".ops").hide();
    });
    $(".goal-wrap .ops .edit").on("click", function() {
        $("#goal-edit-modal").addClass("modal").removeClass("empty");
        $("#goal-edit-modal #goal-edit-wrap").css("margin-top", "-500px");
        $("#goal-edit-modal #goal-edit-wrap").animate({"margin-top": 10}, 500);
    });
    $("#add-goal").on("click", function () {
        $("#goal-add-modal").addClass("modal").removeClass("empty");
        $("#goal-add-modal #goal-add-wrap").css("margin-top", "-500px");
        $("#goal-add-modal #goal-add-wrap").animate({"margin-top": 10}, 500);
    });
    $(".todo-wrap .todo-ops .edit").on("click", function() {
        $("#todo-edit-modal").addClass("modal").removeClass("empty");
        $("#todo-edit-modal #todo-edit-wrap").css("margin-top", "-500px");
        $("#todo-edit-modal #todo-edit-wrap").animate({"margin-top": 10}, 500);
    });
    $(".goal-wrap .ops .add-todo").on("click", function() {
        $(this).parents(".goal-wrap").find(".add-todo-wrap .name-input").show().focus();
    });
    $(".add-todo-wrap .name-input").on("blur", function() {
        $(this).hide();
    });
    $(".add-todo-wrap .name-input").on("keydown", function(event) {
        if(event.keyCode==13) {
            alert("add success");
        }
    })
})