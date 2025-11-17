{
    "name": "Proforma Invoice for coptronix ",
    "summary": """Proforma Invoice for coptronix """,
    "description": """Proforma Invoice for coptronix """,
    "category": "Accounting/Localizations/Reporting",
    "version": "1.0.2",
    "author": "Wahab Safi",
    "website": "https://github.com/wahabsafi",
    "license": "AGPL-3",
    "depends": ["base", "account_reports", "sale", "web","stock"],
    "data": [
        "reports/proforma_invoice_template.xml",
        "reports/paper_formats.xml",
        "views/report_actions.xml",
        "views/sale_order.xml",
    ],
    "assets": {
        "web.report_assets_common": [
            "proforma_invoice/static/src/scss/fonts.scss",
            "proforma_invoice/static/src/css/style.css",
        ],
        "web.report_assets_pdf": [
            "proforma_invoice/static/src/scss/fonts.scss",
            "proforma_invoice/static/src/css/style.css",
            "proforma_invoice/static/src/scss/style.scss",
        ],
    },
    "installable": True,
}
