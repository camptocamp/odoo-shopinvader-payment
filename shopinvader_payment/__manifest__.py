# Copyright 2017 Akretion (http://www.akretion.com)
# Sébastien BEAU <sebastien.beau@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Shopinvader Payment",
    "summary": "Payment integration for Shopinvader",
    "version": "12.0.1.0.0",
    "category": "e-commerce",
    "website": "https://akretion.com",
    "author": "Akretion",
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "external_dependencies": {"python": ["cerberus", "unidecode"], "bin": []},
    "depends": [
        "account_payment_mode",
        "account_payment_sale",
        "shopinvader",
        "sale_automatic_workflow_payment_mode",
        "onchange_helper",
        "invader_payment",
    ],
    "data": [
        "views/shopinvader_menu.xml",
        "views/shopinvader_payment_view.xml",
        "views/account_payment_mode.xml",
        "views/backend_view.xml",
        "security/ir.model.access.csv",
    ],
    "demo": ["demo/payment_demo.xml"],
    "qweb": [],
}
