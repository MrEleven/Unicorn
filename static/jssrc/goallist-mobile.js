/**
 * Created by eleven on 15-12-8.
 */

avalon.filters.money = function(amount) {
    amount = amount / 100;
    return avalon.filters.number(amount, 2, '.', ',');
};
avalon.filters.redeemStatus = function(status) {
    if (status == 0) {
        return "待兑付";
    }
    if (status == 1) {
        return "需兑付";
    }
    if (status == 2) {
        return "兑付中";
    }
    if (status == 3) {
        return "已兑付";
    }
    if (status == 4) {
        return "无需兑付";
    }
};
var now = new Date();
var endtimestr = now.Format("yyyy-MM-dd");
now.setDate(now.getDate() - 5);
var starttimestr = now.Format("yyyy-MM-dd");
var listModel = avalon.define({
    $id: "list",
    $url: "/creditguard/settle/product",
    page: {
        pageList: []
    },
    list: [],
    startTime: starttimestr,
    endTime: endtimestr,
    $updateModel: function(ajaxData) {
        var model = listModel;
        $.each(ajaxData.list, function(i, val) {
            val.checked = false;
        });
        avalon.vmMix(true, model, ajaxData);
        avalon.scan($("#list")[0], model);
    },
    $search: function() {
        $.ajax({
            url: "/creditguard/settle/product",
            type: "GET",
            data: encodeURI($("#searchForm").serialize()),
            dataType: "json",
            contentType: "application/json; charset=utf-8"
        }).done(function(ajaxData) {
            if (ajaxData.status == 200) {
                ajaxData = ajaxData.data;
                ajaxData.page = av.createPageInfo(ajaxData.page); // 生成avalon翻页数据
                listModel.$updateModel(ajaxData);
            } else {
                alert(ajaxData.msg);
            }
        });
    },
    $settle: function() {
        var productCode = $(this).attr("data-productcode"),
            bool = confirm("确定执行"+ productCode +"的兑付操作么?");

        if (bool) {
            $.ajax({
                type: "POST",
                url: "/creditguard/redeem",
                data: "productCode=" + productCode,
                dataType: "json"
            }).done(function(data) {
                if (data.status != 200) {
                    alert(data.msg);
                } else {
                    alert("兑付成功!");
                    listModel.$search();
                }
            }).fail(function(err) {
                alert(err.responseText);
            });
        }
    }
});
