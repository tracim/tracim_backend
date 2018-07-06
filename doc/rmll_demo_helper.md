

# create user

tracimcli user create -l "john@doe.test" -p johnjohn

# create workspace

curl -u admin@admin.admin:admin@admin.admin -X POST "http://localhost:6543/api/v2/workspaces" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"description\": \"A super description of my workspace.\",  \"label\": \"My Workspace\"}"

# add role to user in workspace 1

curl -u admin@admin.admin:admin@admin.admin -X POST "http://localhost:6543/api/v2/workspaces/1/members" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"role\": \"contributor\",  \"user_email_or_public_name\": \"john@doe.test\",  \"user_id\": null}"
