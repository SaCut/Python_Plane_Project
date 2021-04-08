from login import Login

object = Login()

# object.hash_password("admin", "admin")
# object.right_password("admin", "admin")
print(object.right_password("admin", object.hash_password("admin", "admin")))
# for _ in range(4):
#     print(object.hash_password("admin", "admin"))

"bknx9dnx96nxcc[oSnx9anx98nxd9nx02k"
"bknx9dnx96nxcc[oSnx9anx98nxd9nx02k"