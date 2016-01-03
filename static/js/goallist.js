/**
 * Created by eleven on 15-11-1.
 */
"use strict";

ReactDOM.render(React.createElement(
    "h1",
    null,
    "Hello, world!"
), document.getElementById("main"));

var EMPTYGOAL = { "id": 0, "name": "", "description": "", "image": "", "create_time": "", "status": 1 };
var EMPTYTODO = { "id": 0, "goal_id": 0, "name": "", "note": "", "create_time": "", "status": 1 };

var TodoEditModal = React.createClass({
    displayName: "TodoEditModal",

    getInitialState: function getInitialState() {
        return { data: EMPTYTODO };
    },
    cancelClick: function cancelClick(event) {
        this.setState({ data: EMPTYTODO });
    },
    editClick: function editClick(event) {
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var todo_id = this.state.data.id;
        var goal_id = this.state.data.goal_id;
        var name = this.refs.name.value.trim();
        var note = this.refs.note.value.trim();
        var todo_info = { "todo_id": todo_id, "goal_id": goal_id, "name": name, "note": note, "_xsrf": _xsrf };
        $.ajax({
            url: '/a/todo/update',
            dataType: 'json',
            type: 'POST',
            data: todo_info,
            success: (function (data) {
                console.log("post success");
                this.props.editCallback();
                this.setState({ data: EMPTYTODO });
            }).bind(this),
            error: (function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }).bind(this)
        });
    },
    handleChange: function handleChange(event) {
        var data = this.state.data;
        data.name = this.refs.name.value;
        data.note = this.refs.note.value;
        this.setState({ data: data });
    },
    render: function render() {
        return React.createElement(
            "div",
            { id: "todo-edit-modal", className: this.state.data.id ? "modal" : "empty" },
            React.createElement(
                "section",
                { id: "todo-edit-wrap", className: "todo-edit-wrap" },
                React.createElement(
                    "span",
                    null,
                    "名称"
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement("input", { className: "name-input", ref: "name", type: "text", name: "name", onChange: this.handleChange, value: this.state.data.name })
                ),
                React.createElement(
                    "span",
                    null,
                    "备注信息"
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement("textarea", { name: "note", className: "note-input", ref: "note", onChange: this.handleChange, value: this.state.data.note, placeholder: "没什么重要东西需要备注的就不要写了" })
                ),
                React.createElement(
                    "div",
                    { className: "ops" },
                    React.createElement(
                        "button",
                        { id: "todo-edit-save-btn", onClick: this.editClick },
                        "保存"
                    ),
                    React.createElement(
                        "button",
                        { id: "todo-edit-cancel-btn", onClick: this.cancelClick },
                        "取消"
                    )
                )
            )
        );
    }
});

var GoalEditModal = React.createClass({
    displayName: "GoalEditModal",

    getInitialState: function getInitialState() {
        return { data: EMPTYGOAL };
    },
    cancelClick: function cancelClick(event) {
        this.setState({ data: EMPTYGOAL });
    },
    handleChange: function handleChange(event) {
        var data = this.state.data;
        data.name = this.refs.name.value;
        data.description = this.refs.description.value;
        this.setState({ data: data });
    },
    editClick: function editClick(event) {
        var goal_id = this.state.data.id;
        var image = this.refs.album.src;
        var name = this.refs.name.value.trim();
        var description = this.refs.description.value.trim();
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var goal_info = { "goal_id": goal_id, "image": image, "name": name, "description": description, "_xsrf": _xsrf };

        $.ajax({
            url: '/a/goal/update',
            dataType: 'json',
            type: 'POST',
            data: goal_info,
            success: (function (data) {
                console.log("post success");
                this.props.editCallback();
                this.setState({ data: EMPTYGOAL });
            }).bind(this),
            error: (function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }).bind(this)
        });
    },
    render: function render() {
        return React.createElement(
            "div",
            { id: "goal-edit-modal", className: this.state.data.id ? "modal" : "empty" },
            React.createElement(
                "section",
                { id: "goal-edit-wrap", className: "goal-edit-wrap", "goal-id": "0" },
                React.createElement(
                    "span",
                    null,
                    "图片"
                ),
                React.createElement(
                    "div",
                    { className: "album-wrap" },
                    React.createElement("img", { className: "album", id: "goal-edit-wrap-album", ref: "album", src: this.state.data.image, alt: "avatar image" })
                ),
                React.createElement(
                    "span",
                    null,
                    "目标名称"
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement("input", { className: "name-input", ref: "name", type: "text", name: "name", onChange: this.handleChange, value: this.state.data.name })
                ),
                React.createElement(
                    "span",
                    null,
                    "描述"
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement("textarea", { name: "desc", className: "desc-input", ref: "description", onChange: this.handleChange, value: this.state.data.description })
                ),
                React.createElement(
                    "div",
                    { className: "ops" },
                    React.createElement(
                        "button",
                        { id: "goal-edit-save-btn", onClick: this.editClick },
                        "保存"
                    ),
                    React.createElement(
                        "button",
                        { id: "goal-edit-cancel-btn", onClick: this.props.hideCallback },
                        "取消"
                    )
                )
            )
        );
    }
});

var GoalAddModal = React.createClass({
    displayName: "GoalAddModal",

    getInitialState: function getInitialState() {
        return { visiablity: false };
    },
    cancelClick: function cancelClick(event) {
        this.setState({ visiablity: false });
    },
    addClick: function addClick(event) {
        var name = this.refs.name.value.trim();
        var desc = this.refs.desc.value.trim();
        var album = this.refs.album.src.trim();
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var goal_info = { "name": name, "description": desc, "_xsrf": _xsrf, "image": album };
        $.ajax({
            url: '/a/goal/add',
            dataType: 'json',
            type: 'POST',
            data: goal_info,
            success: (function (data) {
                this.setState({ visiablity: false });
                this.props.addCallback();
            }).bind(this),
            error: (function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }).bind(this)
        });
    },
    componentDidMount: function componentDidMount() {
        this.refs.name.value = "";
        this.refs.desc.value = "";
    },
    componentDidUpdate: function componentDidUpdate() {
        this.refs.name.value = "";
        this.refs.desc.value = "";
    },
    render: function render() {
        return React.createElement(
            "div",
            { id: "goal-add-modal", className: this.state.visiablity ? "modal" : "empty" },
            React.createElement(
                "section",
                { id: "goal-add-wrap", className: "goal-edit-wrap" },
                React.createElement(
                    "span",
                    null,
                    "图片"
                ),
                React.createElement(
                    "div",
                    { className: "album-wrap" },
                    React.createElement("img", { className: "album", ref: "album", id: "add-goal-modal-album", src: "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", alt: "avatar image" })
                ),
                React.createElement(
                    "span",
                    null,
                    "目标名称"
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement("input", { className: "name-input", type: "text", name: "name", ref: "name" })
                ),
                React.createElement(
                    "span",
                    null,
                    "描述"
                ),
                React.createElement(
                    "div",
                    null,
                    React.createElement("textarea", { name: "desc", className: "desc-input", ref: "desc" })
                ),
                React.createElement(
                    "div",
                    { className: "ops" },
                    React.createElement(
                        "button",
                        { id: "goal-add-save-btn", onClick: this.addClick },
                        "添加"
                    ),
                    React.createElement(
                        "button",
                        { id: "goal-add-cancel-btn", onClick: this.cancelClick },
                        "取消"
                    )
                )
            )
        );
    }
});

var AddTodoWrap = React.createClass({
    displayName: "AddTodoWrap",

    getInitialState: function getInitialState() {
        return { visiablity: false };
    },
    componentDidUpdate: function componentDidUpdate() {
        if (this.state.visiablity) {
            this.nameInput.focus();
        }
    },
    hiddenWrap: function hiddenWrap() {
        var name = this.nameInput.value;
        this.setState({ visiablity: false });
    },
    enter: function enter(event) {
        if (event.keyCode == 13) {
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            var name = this.nameInput.value;
            if (name) {
                var todo_info = { "_xsrf": _xsrf, "name": name };
                this.props.onEnter(todo_info);
                this.nameInput.value = "";
                this.setState({ visiablity: false });
            }
        };
    },
    render: function render() {
        var _this = this;

        return React.createElement(
            "div",
            { className: this.state.visiablity ? "add-todo-input-wrap" : "empty" },
            React.createElement("input", { type: "text", ref: function (ref) {
                    return _this.nameInput = ref;
                }, onBlur: this.hiddenWrap, onKeyDown: this.enter, className: "name-input", placeholder: "按Enter键盘完成添加" })
        );
    }
});

var Todo = React.createClass({
    displayName: "Todo",

    editClick: function editClick(event) {
        this.props.onTodoEditClick(this.props.data);
    },
    deleteClick: function deleteClick(event) {
        if (confirm("确定要删除这个待办事项吗，年轻人？")) {
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            var params = { "todo_id": this.props.data.id, "_xsrf": _xsrf };
            $.ajax({
                url: '/a/todo/delete',
                dataType: 'json',
                type: 'POST',
                data: params,
                success: (function (data) {
                    this.props.loadTodoList();
                }).bind(this)
            });
        }
    },
    finishClick: function finishClick(event) {
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var params = { "todo_id": this.props.data.id, "_xsrf": _xsrf };
        var url = "/a/todo/unfinish";
        if (this.props.data.status == 1) {
            url = "/a/todo/finish";
        }
        $.ajax({
            url: url,
            dataType: 'json',
            type: 'POST',
            data: params,
            success: (function (data) {
                this.props.loadTodoList();
            }).bind(this)
        });
    },
    render: function render() {
        return React.createElement(
            "li",
            { className: "todo-wrap" },
            React.createElement("div", { className: "finish " + (this.props.data.status == 1 ? "unfinish-icon" : "finished-icon"), onClick: this.finishClick }),
            React.createElement(
                "span",
                { className: "todo-name" },
                this.props.data.name
            ),
            React.createElement(
                "div",
                { className: "todo-ops" },
                React.createElement(
                    "a",
                    { className: "edit", onClick: this.editClick },
                    "编辑"
                ),
                " | ",
                React.createElement(
                    "a",
                    { className: "delete", onClick: this.deleteClick },
                    "删除"
                )
            )
        );
    }
});

var TodoList = React.createClass({
    displayName: "TodoList",

    render: function render() {
        var onTodoEditClick = this.props.onTodoEditClick;
        var todo_list = this.props.data.map((function (todo) {
            return React.createElement(Todo, { key: todo.id, data: todo, loadTodoList: this.props.loadTodoList, onTodoEditClick: onTodoEditClick });
        }).bind(this));
        return React.createElement(
            "ul",
            { className: "todo-list-ul" },
            todo_list
        );
    }
});

var GoalInfo = React.createClass({
    displayName: "GoalInfo",

    render: function render() {
        return React.createElement(
            "div",
            { className: "goal-info" },
            React.createElement(
                "div",
                { className: "goal-icon-wrap" },
                React.createElement("img", { className: "goal-icon", src: this.props.data.image, alt: "goal-icon" })
            ),
            React.createElement(
                "div",
                { className: "goal-info-rwrap" },
                React.createElement(
                    "div",
                    { className: "goal-name" },
                    this.props.data.name
                ),
                React.createElement(
                    "p",
                    { className: "goal-desc" },
                    this.props.data.description
                )
            )
        );
    }
});

var GoalWrap = React.createClass({
    displayName: "GoalWrap",

    getInitialState: function getInitialState() {
        return { data: [] };
    },
    addTodoEnter: function addTodoEnter(todo_info) {
        todo_info["goal_id"] = this.props.data.id;
        $.ajax({
            url: '/a/todo/add',
            dataType: 'json',
            type: 'POST',
            data: todo_info,
            success: (function (data) {
                console.log("comming");
                console.log("cool data is" + JSON.stringify(data));
                this.loadTodoList();
            }).bind(this)
        });
    },
    loadTodoList: function loadTodoList() {
        $.ajax({
            url: '/a/todo/list?goal_id=' + this.props.data.id,
            dataType: 'json',
            success: (function (data) {
                console.log("from server get data " + JSON.stringify(data));
                this.setState({ data: data["result"] });
            }).bind(this),
            error: (function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }).bind(this)
        });
    },
    showAddTodoWrap: function showAddTodoWrap() {
        this.refs.AddTodoWrap.setState({ visiablity: true });
    },
    editClick: function editClick(event) {
        this.props.onGoalEditClick(this.props.data);
    },
    deleteClick: function deleteClick(event) {
        if (confirm("确定要删除这个目标吗，年轻人？(会把目标中的待办事项一起删除掉哦)")) {
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            var params = { "goal_id": this.props.data.id, "_xsrf": _xsrf };
            $.ajax({
                url: '/a/goal/delete',
                dataType: 'json',
                type: 'POST',
                data: params,
                success: (function (data) {
                    this.props.loadGoalListFromServer();
                }).bind(this)
            });
        }
    },
    componentDidMount: function componentDidMount() {
        this.loadTodoList();
    },
    render: function render() {
        return React.createElement(
            "li",
            { id: "goal-" + this.props.data.id, className: "goal-wrap", "goal-id": this.props.data.id },
            React.createElement(
                "div",
                { className: "ops" },
                React.createElement(
                    "a",
                    { className: "add-todo", onClick: this.showAddTodoWrap },
                    "增加代办事项"
                ),
                " ｜ ",
                React.createElement(
                    "a",
                    { className: "edit", id: "123", onClick: this.editClick },
                    "编辑"
                ),
                " | ",
                React.createElement(
                    "a",
                    { className: "delete", onClick: this.deleteClick },
                    "删除"
                )
            ),
            React.createElement(GoalInfo, { data: this.props.data }),
            React.createElement(TodoList, { data: this.state.data || [], loadTodoList: this.loadTodoList, onTodoEditClick: this.props.onTodoEditClick }),
            React.createElement(
                "div",
                { className: "add-todo-wrap" },
                React.createElement(
                    "div",
                    { className: "add-todo-button-wrap", onClick: this.showAddTodoWrap },
                    "点击增加待办事项"
                ),
                React.createElement(AddTodoWrap, { ref: "AddTodoWrap", goal_id: this.props.data.id, onEnter: this.addTodoEnter })
            )
        );
    }
});

var GoalList = React.createClass({
    displayName: "GoalList",

    render: function render() {
        var goal_list = this.props.data.map((function (goal) {
            return React.createElement(GoalWrap, { key: goal.id, loadGoalListFromServer: this.props.loadGoalListFromServer, data: goal, onGoalEditClick: this.props.onGoalEditClick, onTodoEditClick: this.props.onTodoEditClick });
        }).bind(this));
        return React.createElement(
            "section",
            { id: "goal-list-wrap" },
            React.createElement(
                "ul",
                { id: "goal-list-ul" },
                goal_list
            )
        );
    }
});

var GoalListNav = React.createClass({
    displayName: "GoalListNav",

    render: function render() {
        var goal_list = this.props.data.map((function (goal) {
            return React.createElement(
                "li",
                { key: goal.id },
                React.createElement(
                    "a",
                    { "data-goal-id": goal.id },
                    goal.name
                )
            );
        }).bind(this));
        return React.createElement(
            "nav",
            { id: "goal-nav" },
            React.createElement(
                "ul",
                null,
                goal_list
            ),
            React.createElement(
                "div",
                null,
                React.createElement(
                    "a",
                    { id: "add-goal", onClick: this.props.onAddGoalClick },
                    "增加目标"
                )
            )
        );
    }
});

var GoalListWrap = React.createClass({
    displayName: "GoalListWrap",

    getInitialState: function getInitialState() {
        return { data: [] };
    },
    showAddGoalModal: function showAddGoalModal() {
        this.refs.goalAddModal.setState({ visiablity: true });
    },
    showGoalEditModal: function showGoalEditModal(data) {
        this.refs.goalEditModal.setState({ data: data });
    },
    hiddenGoalEditModal: function hiddenGoalEditModal() {
        this.refs.goalEditModal.setState({ data: EMPTYGOAL });
    },
    showTodoEditModal: function showTodoEditModal(data) {
        this.refs.todoEditModal.setState({ data: data });
    },
    loadGoalListFromServer: function loadGoalListFromServer() {
        $.ajax({
            url: '/a/goal/list',
            dataType: 'json',
            cache: false,
            success: (function (data) {
                console.log("from server get data " + JSON.stringify(data));
                this.setState({ data: data["result"] });
            }).bind(this),
            error: (function (xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }).bind(this)
        });
    },
    componentDidMount: function componentDidMount() {
        this.loadGoalListFromServer();
    },
    render: function render() {
        return React.createElement(
            "div",
            null,
            React.createElement(GoalList, { data: this.state.data, loadGoalListFromServer: this.loadGoalListFromServer, onGoalEditClick: this.showGoalEditModal, onTodoEditClick: this.showTodoEditModal }),
            React.createElement(GoalAddModal, { ref: "goalAddModal", addCallback: this.loadGoalListFromServer }),
            React.createElement(GoalEditModal, { ref: "goalEditModal", hideCallback: this.hiddenGoalEditModal, editCallback: this.loadGoalListFromServer }),
            React.createElement(TodoEditModal, { ref: "todoEditModal", editCallback: this.loadGoalListFromServer }),
            React.createElement(GoalListNav, { data: this.state.data, onAddGoalClick: this.showAddGoalModal })
        );
    }
});

//var goal_list = [
//    {"id": 1, "name": "资深前端工程师", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 2, "name": "资深UDE", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 3, "name": "资深Python工程师", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 4, "name": "资深产品经理", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 5, "name": "资深运帷工程师", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"}
//];

document.body.addEventListener('touchstart', function () {});
$(function () {
    function click_scroll(obj_id) {
        var scroll_offset = $(obj_id).offset();
        $("body").animate({
            scrollTop: scroll_offset.top - 15
        }, 250);
    };
    $(document).on("click", "#goal-nav ul a", function () {
        var goal_id = $(this).attr("data-goal-id");
        var target_id = "#goal-" + goal_id;
        click_scroll(target_id);
    });
    var goal_list = [];
    ReactDOM.render(React.createElement(GoalListWrap, { data: goal_list }), document.getElementById("main"));

    var _xsrf = $("#_xsrf input[name=_xsrf]").val();
    var uploader = new plupload.Uploader({
        browse_button: 'add-goal-modal-album',
        url: '/a/image/upload',
        multipart_params: {
            "_xsrf": _xsrf
        }
    });
    uploader.init();
    //绑定各种事件，并在事件监听函数中做你想做的事
    uploader.bind('FilesAdded', function (uploader, files) {
        console.log("start upload");
        uploader.start();
    });
    uploader.bind('FileUploaded', function (uploader, file, resp) {
        console.log(resp.response);
        $("#add-goal-modal-album").attr("src", JSON.parse(resp.response)["result"]);
    });

    var uploaderEditGoal = new plupload.Uploader({
        browse_button: 'goal-edit-wrap-album',
        url: '/a/image/upload',
        multipart_params: {
            "_xsrf": _xsrf
        }
    });
    uploaderEditGoal.init();
    //绑定各种事件，并在事件监听函数中做你想做的事
    uploaderEditGoal.bind('FilesAdded', function (uploader, files) {
        console.log("start upload");
        uploaderEditGoal.start();
    });
    uploaderEditGoal.bind('FileUploaded', function (uploader, file, resp) {
        console.log(resp.response);
        $("#goal-edit-wrap-album").attr("src", JSON.parse(resp.response)["result"]);
    });
});
