# addUser = [
#     Check("username").isString().minLength(
#         3).maxLength(24).notEmpty().required(),
#     Check("password").isPassword().notEmpty().required(),
#     Check("firstName").isString().maxLength(32).notEmpty().required(),
#     Check("lastName").isString().maxLength(32).notEmpty().required(),
#     Check("gender").includes(CONST.ENUM.GENDER),
#     Check("userType").includes(CONST.ENUM.USER_TYPE),
#     Check("gender").includes(CONST.ENUM.GENDER).required(),
#     Check("userType").includes(CONST.ENUM.USER_TYPE).required(),
#     Check("phoneNumber").isString().minLength(10).maxLength(13),
#     Check("email").isEmail().notEmpty().required(),
# ]

# default(addUser)
# loginUser = [
#     Check("username").isString().minLength(3).maxLength(24).notEmpty(),
#     Check("password").isPassword().notEmpty().required(),
#     Check("email").isEmail().notEmpty(),
# ]

# updateUser = [
#     Check("username").isString().minLength(3).maxLength(24).notEmpty(),
#     Check("firstName").isString().maxLength(32).notEmpty(),
#     Check("lastName").isString().maxLength(32).notEmpty(),
#     Check("gender").includes(CONST.ENUM.GENDER),
#     Check("userType").includes(CONST.ENUM.USER_TYPE),
#     Check("phoneNumber").isString().minLength(10).maxLength(13),
#     Check("email").isEmail().notEmpty(),
# ]
# export(default(addUser, loginUser, updateUser))
