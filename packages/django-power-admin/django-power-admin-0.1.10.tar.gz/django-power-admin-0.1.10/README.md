# django-power-admin

Django提供了快捷的生成后台管理站点的能力。本应用旨在增强Django Admin的能力，提供丰富的Admin、Widget、ListFilter、Form等等界面扩展类，同时也为常用的数据管理模型提供完整的管理功能。

## 功能扩展清单

### Admin后台管理界面整体控制

| 主要功能 |
| -------- |
| `@todo` 定制化的登录界面 |
| `@todo` 登录框增加图形验证码 |
| `@todo` 登录后增加短信验证 |
| `@todo` 顶部导航 |
| `@todo` 左侧导航 |
| `@todo` 首页控制面板 |
| `@todo` 应用模块级控制面板 |
| `@todo` 用户中心子站 |
| `@todo` 中国风的组织架构管理和用户管理 |

### Admin扩展类

| 类名 | 主要功能 |
| ---- | -------- |
| PowerAdmin | 提供辅助方法，便于后续ModelAdmin扩展开发。 |

### Admin辅助函数
| 函数名 | 主要功能 |
| ---- | -------- |
| add_extra_css | 为当前页添加额外的css代码段 |
| add_extra_js | 为当前页添加额外的js代码段 |


### Widget扩展类

| 类名 | 主要功能 |
| ---- | -------- |
| Select2 | 将标准select下拉框转为select2样式下拉框 |
| SelectMultiple2 | 将标准select复选框转为select2样式下拉式复选框 |
| `@todo` PasswordResetableWidget | 密码重置字段（只重置，不显示）|

### Field扩展类

| 类名 | 主要功能 |
| ---- | -------- |
| MPTTModelChoiceField | MPTT数据模型中的Parent字段关联的表单字段，<br />使用Select2样式控件。<br />建议在MPTTAdminForm中使用 |
| ModelChoiceFieldWithLabelProperty | 标准ModelChoiceField的扩展，<br />支持使用自定义的标签函数 |

### Form扩展类

### ListFilter扩展类

### 数据模型

## 版本记录

### v0.1.0 2021/07/11

- 项目启动。
- 框架搭建。

### v0.1.7 2021/12/23 （首次发布）

- PowerAdmin类基本完成。

### v0.1.10 2021/12/24

- get_extra_views更名为get_extra_view_urls，避免与其它方法名冲突。
- view_action更名为read_xxx。xxx_action更名为xxx_button。
- 在list_display中追加change_list_object_toolbar字段。
