# Problem Statement – Smart Campus Lost-and-Found Management System

## Problem Statement
On a busy campus, students regularly lose personal belongings such as notebooks, jewellery, ID cards and water bottles, while others find items and are unsure whom to hand them to. Reports are usually passed on by word of mouth, group chats or paper notices, which are easy to miss, hard to search, and never marked as closed once an item is returned. As a result, owners and finders rarely connect, and the same item is asked about again and again.

This project provides a simple, organised digital system in which lost and found items can be reported in one place, searched quickly, and marked as claimed once resolved.

## Scope of the Project
**In scope**
- Reporting an item as *Lost* or *Found* with name, description, location and reporter name
- Validating user input (item type, empty fields, report numbers)
- Viewing all reports with their status (Open / Claimed)
- Searching reports by item name, description or location
- Marking a report as claimed/resolved and removing a report
- Showing open, resolved, total, lost and found counts
- A menu-driven console interface written in Python using a modular design

**Out of scope (in the current version)**
- Permanent storage (database or files); data lives in memory while the program runs
- User accounts, login and role-based permissions
- Image uploads, notifications (email/SMS) and a graphical or web interface
- Automatic matching of lost items with found items

## Target Users
- **Students** who have lost an item or have found one
- **Campus staff / security / lost-and-found desk** who keep track of reported items and close them once returned
- **Faculty and visitors** who want a single place to report or look for belongings

## High-Level Features
1. Report a lost or found item
2. View all reports with status
3. Search by name, description or location
4. Claim / resolve an item
5. Remove a report
6. View report counts (total, lost, found, open, resolved)
7. Input validation with clear error messages
8. Modular code structure (`main.py`, `check.py`, `item.py`, `lost_found_manager.py`)
