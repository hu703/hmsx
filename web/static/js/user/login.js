;
var user_login_ops = {
    init:function(){
        this.eventBind()
        console.log('aaaa')
    },
    eventBind:function(){
        $('.login_wrap .do-login').click(function(){
            console.log('click')
            var login_name = $('.login_wrap input[name=login_name]').val()
            var login_pwd = $('.login_wrap input[name=login_pwd]').val()

            console.log(login_name)
            console.log(login_pwd)
        })
    }
}
$(document).ready(function(){
    user_login_ops.init()
})