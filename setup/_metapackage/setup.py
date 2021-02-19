import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-account-financial-tools",
    description="Meta package for oca-account-financial-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_asset_management',
        'odoo13-addon-account_balance_line',
        'odoo13-addon-account_cash_basis_group_base_line',
        'odoo13-addon-account_chart_update',
        'odoo13-addon-account_check_deposit',
        'odoo13-addon-account_fiscal_position_allowed_journal',
        'odoo13-addon-account_fiscal_year',
        'odoo13-addon-account_journal_lock_date',
        'odoo13-addon-account_lock_date_update',
        'odoo13-addon-account_lock_to_date',
        'odoo13-addon-account_menu',
        'odoo13-addon-account_move_budget',
        'odoo13-addon-account_move_force_removal',
        'odoo13-addon-account_move_line_purchase_info',
        'odoo13-addon-account_move_line_tax_editable',
        'odoo13-addon-account_move_template',
        'odoo13-addon-account_netting',
        'odoo13-addon-account_tax_repartition_line_tax_group_account',
        'odoo13-addon-base_vat_optional_vies',
        'odoo13-addon-product_category_tax',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
