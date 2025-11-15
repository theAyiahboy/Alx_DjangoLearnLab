# Bookshelf Permissions System

This project demonstrates how to implement custom permissions and groups in Django.
The Book model includes the following permissions:

- can_view
- can_create
- can_edit
- can_delete

## Groups
Using the Django admin site, the following groups can be created:
- Viewers (can_view)
- Editors (can_view, can_edit, can_create)
- Admins (all permissions including can_delete)

## Views
Views use the permission_required decorator to enforce access control.
Example:
@permission_required('bookshelf.can_edit')

## How to Test
1. Create users
2. Assign them to groups
3. Log in and test restricted views

This setup provides secure role-based access for the application.
