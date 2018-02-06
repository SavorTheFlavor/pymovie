from . import admin  # import admin blueprint
from flask import render_template,url_for,redirect


@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("/login")
def login():
    return render_template("admin/login.html")

@admin.route("/logout")
def logout():
    return render_template("admin/logout.html")

@admin.route("/pwd")
def pwd():
    return render_template("admin/pwd.html")

# 添加标签
@admin.route("/tag/add/", methods=["GET", "POST"])
def tag_add():
    return render_template("admin/tag_add.html")


# 编辑标签
@admin.route("/tag/edit/<int:id>/", methods=["GET", "POST"])
def tag_edit(id=None):
    return render_template("admin/tag_edit.html")


# 标签列表
@admin.route("/tag/list/<int:page>/", methods=["GET"])
def tag_list(page=None):
    return render_template("admin/tag_list.html")


# 标签删除
@admin.route("/tag/del/<int:id>/", methods=["GET"])
def tag_del(id=None):
    return redirect(url_for('admin.tag_list', page=1))


# 添加电影
@admin.route("/movie/add/", methods=["GET", "POST"])
def movie_add():
    return render_template("admin/movie_add.html")


# 电影列表
@admin.route("/movie/list/<int:page>/", methods=["GET"])
def movie_list(page=None):
    return render_template("admin/movie_list.html")


# 删除电影
@admin.route("/movie/del/<int:id>/", methods=["GET"])
def movie_del(id=None):
    return redirect(url_for('admin.movie_list', page=1))


# 编辑电影
@admin.route("/movie/edit/<int:id>/", methods=["GET", "POST"])
def movie_edit(id=None):
    return render_template("admin/movie_edit.html")


# 添加预告
@admin.route("/preview/add/", methods=["GET", "POST"])
def preview_add():
    return render_template("admin/preview_add.html")


# 预告列表
@admin.route("/preview/list/<int:page>/", methods=["GET"])
def preview_list(page=None):
    return render_template("admin/preview_list.html")


# 删除预告
@admin.route("/preview/del/<int:id>/", methods=["GET"])
def preview_del(id=None):
    return redirect(url_for('admin.preview_list', page=1))


# 编辑预告
@admin.route("/preview/edit/<int:id>/", methods=["GET", "POST"])
def preview_edit(id):
    return render_template("admin/preview_edit.html")


# 会员列表
@admin.route("/user/list/<int:page>/", methods=["GET"])
def user_list(page=None):
    return render_template("admin/user_list.html")


# 查看会员
@admin.route("/user/view/<int:id>/", methods=["GET"])
def user_view(id=None):
    return render_template("admin/user_view.html")


# 删除会员
@admin.route("/user/del/<int:id>/", methods=["GET"])
def user_del(id=None):
    return redirect(url_for('admin.user_list', page=1))


# 评论列表
@admin.route("/comment/list/<int:page>/", methods=["GET"])
def comment_list(page=None):
    return render_template("admin/comment_list.html")


# 删除评论
@admin.route("/comment/del/<int:id>/", methods=["GET"])
def comment_del(id=None):
    return redirect(url_for('admin.comment_list', page=1))


# 收藏列表
@admin.route("/moviecol/list/<int:page>/", methods=["GET"])
def moviecol_list(page=None):
    return render_template("admin/moviecol_list.html")


# 收藏删除
@admin.route("/moviecol/del/<int:id>/", methods=["GET"])
def moviecol_del(id=None):
    return redirect(url_for('admin.moviecol_list', page=1))


# 操作日志
@admin.route("/oplog/list/<int:page>/", methods=["GET"])
def oplog_list(page=None):
    return render_template("admin/oplog_list.html")


# 管理员登录日志
@admin.route("/adminloginlog/list/<int:page>/", methods=["GET"])
def adminloginlog_list(page=None):
    return render_template("admin/adminloginlog_list.html")


# 会员登录日志
@admin.route("/userloginlog/list/<int:page>/", methods=["GET"])
def userloginlog_list(page=None):
    return render_template("admin/userloginlog_list.html")


# 添加角色
@admin.route("/role/add/", methods=["GET", "POST"])
def role_add():
    return render_template("admin/role_add.html")


# 编辑角色
@admin.route("/role/edit/<int:id>/", methods=["GET", "POST"])
def role_edit(id=None):
    return render_template("admin/role_edit.html")


# 角色列表
@admin.route("/role/list/<int:page>/", methods=["GET"])
def role_list(page=None):
    return render_template("admin/role_list.html")


# 删除角色
@admin.route("/role/del/<int:id>/", methods=["GET"])
def role_del(id=None):
    return redirect(url_for('admin.role_list', page=1))


# 权限添加
@admin.route("/auth/add/", methods=["GET", "POST"])
def auth_add():
    return render_template("admin/auth_add.html")


# 权限列表
@admin.route("/auth/list/<int:page>/", methods=["GET"])
def auth_list(page=None):
    return render_template("admin/auth_list.html")


# 权限删除
@admin.route("/auth/del/<int:id>/", methods=["GET"])
def auth_del(id=None):
    return redirect(url_for('admin.auth_list', page=1))


# 编辑权限
@admin.route("/auth/edit/<int:id>/", methods=["GET", "POST"])
def auth_edit(id=None):
    return render_template("admin/auth_edit.html")


# 添加管理员
@admin.route("/admin/add/", methods=["GET", "POST"])
def admin_add():
    return render_template("admin/admin_add.html")


# 管理员列表
@admin.route("/admin/list/<int:page>/", methods=["GET"])

def admin_list(page=None):
    return render_template("admin/admin_list.html")

