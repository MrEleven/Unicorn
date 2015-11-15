/**
 * Created by eleven on 15-11-1.
 */
ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById("main")
);

var EMPTYGOAL = {"id": 0, "name": "", "description": "", "image": "", "create_time": "", "status": 1};
var EMPTYTODO = {"id": 0, "goal_id": 0, "name": "", "note": "", "create_time": "", "status": 1};

var TodoEditModal = React.createClass({
    getInitialState: function() {
        return {data : EMPTYTODO};
    },
    cancelClick: function(event) {
        this.setState({data: EMPTYTODO});
    },
    addClick: function(event) {
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var todo_id = this.state.data.id;
        var goal_id = this.state.data.goal_id;
        var name = this.refs.name.value.trim();
        var note = this.refs.note.value.trim();
        var todo_info = {"todo_id": todo_id, "goal_id": goal_id, "name": name, "note": note, "_xsrf": _xsrf};
        $.ajax({
            url: '/a/todo/add',
            dataType: 'json',
            type: 'POST',
            data: todo_info,
            success: function(data) {
                console.log("post success");
                this.props.editCallback();
                this.setState({data: EMPTYTODO});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    handleChange: function (event) {
        var data = this.state.data;
        data.name = this.refs.name.value;
        data.note = this.refs.note.value;
        this.setState({data: data});
    },
    render: function() {
        return (
            <div id="todo-edit-modal" className={this.state.data.id ? "modal": "empty"}>
                <section id="todo-edit-wrap" className="todo-edit-wrap">
                    <span>名称</span>
                    <div><input className="name-input" ref="name" type="text" name="name" onChange={this.handleChange} value={this.state.data.name} /></div>
                    <span>备注信息</span>
                    <div><textarea name="note" className="note-input" ref="note" onChange={this.handleChange} value={this.state.data.note} placeholder="没什么重要东西需要备注的就不要写了"></textarea></div>
                    <div className="ops">
                        <button id="todo-edit-save-btn" onClick={this.addClick} >保存</button>
                        <button id="todo-edit-cancel-btn" onClick={this.cancelClick}>取消</button>
                    </div>
                </section>
            </div>
        );
    }
});


var GoalEditModal = React.createClass({
    getInitialState: function() {
        return {data: EMPTYGOAL};
    },
    cancelClick: function(event) {
        this.setState({data: EMPTYGOAL});
    },
    handleChange: function(event) {
        var data = this.state.data;
        data.name = this.refs.name.value;
        data.description = this.refs.description.value;
        this.setState({data: data});
    },
    editClick: function(event) {
        var goal_id = this.state.data.id;
        var image = this.refs.album.src;
        var name = this.refs.name.value.trim();
        var description = this.refs.description.value.trim();
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var goal_info = {"goal_id": goal_id, "image": image, "name": name, "description": description, "_xsrf": _xsrf};

        $.ajax({
            url: '/a/goal/update',
            dataType: 'json',
            type: 'POST',
            data: goal_info,
            success: function(data) {
                console.log("post success");
                this.props.editCallback();
                this.setState({data: EMPTYGOAL});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    render: function() {
        return (
            <div id="goal-edit-modal" className={this.state.data.id? "modal": "empty"}>
                <section id="goal-edit-wrap" className="goal-edit-wrap" goal-id="0">
                    <span>图片</span>
                    <div className="album-wrap">
                        <img className="album" id="goal-edit-wrap-album" ref="album" src={this.state.data.image} alt="avatar image" />
                    </div>
                    <span>目标名称</span>
                    <div>
                        <input className="name-input" ref="name" type="text" name="name" onChange={this.handleChange} value={this.state.data.name} />
                    </div>
                    <span>描述</span>
                    <div><textarea name="desc" className="desc-input" ref="description" onChange={this.handleChange} value={this.state.data.description}></textarea></div>
                    <div className="ops">
                        <button id="goal-edit-save-btn" onClick={ this.editClick }>保存</button>
                        <button id="goal-edit-cancel-btn" onClick={this.props.hideCallback}>取消</button>
                    </div>
                </section>
            </div>
        );
    }
});


var GoalAddModal = React.createClass({
    getInitialState: function() {
        return {visiablity: false};
    },
    cancelClick: function(event) {
        this.setState({visiablity: false});
    },
    addClick: function(event) {
        var name = this.refs.name.value.trim();
        var desc = this.refs.desc.value.trim();
        var album = this.refs.album.src.trim();
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var goal_info = {"name": name, "description": desc, "_xsrf": _xsrf, "image": album};
        $.ajax({
            url: '/a/goal/add',
            dataType: 'json',
            type: 'POST',
            data: goal_info,
            success: function(data) {
                this.setState({visiablity: false})
                this.props.addCallback();
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    componentDidMount: function () {
        this.refs.name.value = "";
        this.refs.desc.value = "";
    },
    componentDidUpdate: function() {
        this.refs.name.value = "";
        this.refs.desc.value = "";
    },
    render: function() {
        return (
            <div id="goal-add-modal" className={this.state.visiablity? "modal": "empty"}>
                <section id="goal-add-wrap" className="goal-edit-wrap">
                    <span>图片</span>
                    <div className="album-wrap">
                        <img className="album" ref="album" id="add-goal-modal-album" src="http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg" alt="avatar image" />
                    </div>
                    <span>目标名称</span>
                    <div>
                        <input className="name-input" type="text" name="name" ref="name" />
                    </div>
                    <span>描述</span>
                    <div><textarea name="desc" className="desc-input" ref="desc"></textarea></div>
                    <div className="ops">
                        <button id="goal-add-save-btn" onClick={ this.addClick }>添加</button>
                        <button id="goal-add-cancel-btn" onClick={ this.cancelClick }>取消</button>
                    </div>
                </section>
            </div>
        );
    }
});

var AddTodoWrap = React.createClass({
    getInitialState: function() {
        return {visiablity: false};
    },
    componentDidUpdate: function () {
        if (this.state.visiablity) {
            this.nameInput.focus();
        }
    },
    hiddenWrap: function() {
        var name = this.nameInput.value;
        this.setState({visiablity: false});
    },
    enter: function(event) {
        if(event.keyCode==13) {
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            var name = this.nameInput.value;
            if (name) {
                var todo_info = {"_xsrf": _xsrf, "name": name};
                this.props.onEnter(todo_info);
                this.nameInput.value = "";
                this.setState({visiablity: false});
            }
        };
    },
    render: function() {
        return (
            <div className={this.state.visiablity ? "add-todo-wrap": "empty"}>
                <input type="text" ref={(ref) => this.nameInput = ref} onBlur={ this.hiddenWrap } onKeyDown={ this.enter } className="name-input" placeholder="按Enter键盘完成添加" />
            </div>
        )
    }
});

var Todo = React.createClass({
    editClick: function(event) {
        this.props.onTodoEditClick(this.props.data);
    },
    deleteClick: function(event) {
        if(confirm("确定要删除这个待办事项吗，年轻人？")) {
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            var params = {"todo_id": this.props.data.id, "_xsrf": _xsrf};
            $.ajax({
                url: '/a/todo/delete',
                dataType: 'json',
                type: 'POST',
                data: params,
                success: function(data) {
                    this.props.loadTodoList();
                }.bind(this)
            });
        }
    },
    finishClick: function(event) {
        var _xsrf = $("#_xsrf input[name=_xsrf]").val();
        var params = {"todo_id": this.props.data.id, "_xsrf": _xsrf};
        var url = "/a/todo/unfinish";
        if (this.props.data.status == 1) {
            url = "/a/todo/finish";
        }
        $.ajax({
            url: url,
            dataType: 'json',
            type: 'POST',
            data: params,
            success: function(data) {
                this.props.loadTodoList();
            }.bind(this)
        });
    },
    render: function() {
        return (
            <li className="todo-wrap">
                <div className={"finish " + (this.props.data.status == 1? "unfinish-icon" : "finished-icon") } onClick={this.finishClick}></div>
                <span className="todo-name">{this.props.data.name}</span>
                <div className="todo-ops"><a className="edit" onClick={this.editClick }>编辑</a> | <a className="delete" onClick={this.deleteClick}>删除</a></div>
            </li>
        );
    }
});


var TodoList = React.createClass({
    render: function() {
        var onTodoEditClick = this.props.onTodoEditClick;
        var todo_list = this.props.data.map(function(todo) {
            return <Todo key={todo.id} data={todo} loadTodoList={this.props.loadTodoList} onTodoEditClick={onTodoEditClick} />
        }.bind(this));
        return (
            <ul className="todo-list-ul">
                {todo_list}
            </ul>
        );
    }
});


var GoalInfo = React.createClass({
    render: function() {
        return (
            <div className="goal-info">
                <div className="goal-icon-wrap">
                    <img className="goal-icon" src={this.props.data.image} alt="goal-icon" />
                </div>
                <div className="goal-info-rwrap">
                    <div className="goal-name">{this.props.data.name}</div>
                    <p className="goal-desc">{this.props.data.description}</p>
                </div>
            </div>
        );
    }
});


var GoalWrap = React.createClass({
    getInitialState: function() {
        return {data: []};
    },
    addTodoEnter: function(todo_info) {
        todo_info["goal_id"] = this.props.data.id;
        $.ajax({
            url: '/a/todo/add',
            dataType: 'json',
            type: 'POST',
            data: todo_info,
            success: function(data) {
                console.log("comming");
                console.log("cool data is" + JSON.stringify(data));
                this.loadTodoList();
            }.bind(this)
        });
    },
    loadTodoList: function () {
        $.ajax({
            url: '/a/todo/list?goal_id=' + this.props.data.id,
            dataType: 'json',
            success: function(data) {
                console.log("from server get data " + JSON.stringify(data));
                this.setState({data: data["result"]});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    showAddTodoWrap: function() {
        this.refs.AddTodoWrap.setState({visiablity: true});
    },
    editClick: function(event) {
        this.props.onGoalEditClick(this.props.data);
    },
    deleteClick: function(event) {
        if(confirm("确定要删除这个目标吗，年轻人？(会把目标中的待办事项一起删除掉哦)")) {
            var _xsrf = $("#_xsrf input[name=_xsrf]").val();
            var params = {"goal_id": this.props.data.id, "_xsrf": _xsrf};
            $.ajax({
                url: '/a/goal/delete',
                dataType: 'json',
                type: 'POST',
                data: params,
                success: function(data) {
                    this.props.loadGoalListFromServer();
                }.bind(this)
            });
        }
    },
    componentDidMount: function () {
        this.loadTodoList();
    },
    render: function() {
        return (
            <li id={"goal-" + this.props.data.id} className="goal-wrap" goal-id={this.props.data.id}>
                <div className="ops">
                    <a className="add-todo" onClick={ this.showAddTodoWrap }>增加代办事项</a> ｜ <a className="edit" id="123" onClick={this.editClick}>编辑</a> | <a className="delete" onClick={this.deleteClick}>删除</a>
                </div>
                <GoalInfo data={this.props.data} />
                <TodoList data={this.state.data || []} loadTodoList={this.loadTodoList} onTodoEditClick={this.props.onTodoEditClick} />
                <AddTodoWrap ref="AddTodoWrap" goal_id={this.props.data.id} onEnter={this.addTodoEnter} />
            </li>
        );
    }
});


var GoalList = React.createClass({
    render: function() {
        var goal_list = this.props.data.map(function (goal) {
            return (
                <GoalWrap key={goal.id} loadGoalListFromServer={this.props.loadGoalListFromServer} data={goal} onGoalEditClick={ this.props.onGoalEditClick} onTodoEditClick={ this.props.onTodoEditClick} />
            )
        }.bind(this));
        return (
            <section id="goal-list-wrap">
                <ul id="goal-list-ul">
                    {goal_list}
                </ul>
            </section>
        );
    }
});

var GoalListNav = React.createClass({
    render: function() {
        var goal_list = this.props.data.map(function (goal) {
            return (
                <li key={goal.id}><a data-goal-id={goal.id}>{goal.name}</a></li>
            );
        }.bind(this));
        return (<nav id="goal-nav">
            <ul>
                { goal_list }
            </ul>
            <div><a id="add-goal" onClick={this.props.onAddGoalClick}>增加目标</a></div>
        </nav>)
    }
});


var GoalListWrap = React.createClass({
    getInitialState: function() {
        return {data: []};
    },
    showAddGoalModal: function() {
        this.refs.goalAddModal.setState({visiablity: true});
    },
    showGoalEditModal: function(data) {
        this.refs.goalEditModal.setState({data: data});
    },
    hiddenGoalEditModal: function() {
        this.refs.goalEditModal.setState({data: EMPTYGOAL});
    },
    showTodoEditModal: function(data) {
        this.refs.todoEditModal.setState({data: data});
    },
    loadGoalListFromServer: function () {
        $.ajax({
            url: '/a/goal/list',
            dataType: 'json',
            cache: false,
            success: function(data) {
                console.log("from server get data " + JSON.stringify(data));
                this.setState({data: data["result"]});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    componentDidMount: function() {
        this.loadGoalListFromServer();
    },
    render : function() {
        return (<div>
            <GoalListNav data={this.state.data} onAddGoalClick={this.showAddGoalModal} />
            <GoalList data={this.state.data} loadGoalListFromServer={this.loadGoalListFromServer} onGoalEditClick={this.showGoalEditModal} onTodoEditClick={this.showTodoEditModal} />
            <GoalAddModal ref="goalAddModal" addCallback={ this.loadGoalListFromServer } />
            <GoalEditModal ref="goalEditModal" hideCallback={ this.hiddenGoalEditModal } editCallback={ this.loadGoalListFromServer } />
            <TodoEditModal ref="todoEditModal" editCallback={this.loadGoalListFromServer} />
        </div>);
    }
});


//var goal_list = [
//    {"id": 1, "name": "资深前端工程师", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 2, "name": "资深UDE", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 3, "name": "资深Python工程师", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 4, "name": "资深产品经理", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"},
//    {"id": 5, "name": "资深运帷工程师", "todolist": [{"id": 1, "name": "看《javascript权威指南》"}, {"id": 2, "name": "看《超越CSS》"}, {"id": 3, "name": "学习React.Js"}, {"id": 4, "name": "看w3cSchool关于HTML5的手册"}], "image": "http://image.lanrenzhoumo.com/leo/img/20151011162452_2f06eaa77fef3774de0e4f736bcc310b.jpg", "description": "一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。一定要成为牛逼的web前端工程师，跟饺子一样帅。超越可可和乌龙。"}
//];


$(function () {
    function click_scroll(obj_id) {
        var scroll_offset = $(obj_id).offset();
        $("body").animate({
            scrollTop: scroll_offset.top-15
        }, 250);
    };
    $(document).on("click", "#goal-nav ul a", function () {
        var goal_id = $(this).attr("data-goal-id");
        var target_id = "#goal-" + goal_id;
        click_scroll(target_id);
    });
    var goal_list = [];
    ReactDOM.render(
        <GoalListWrap data={goal_list} />,
        document.getElementById("main")
    );


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