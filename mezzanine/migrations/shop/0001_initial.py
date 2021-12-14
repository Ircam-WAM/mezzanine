# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal
import mezzanine.utils.models
import mezzanine.core.fields
import cartridge.shop.fields
<<<<<<< HEAD
import django.db.models.deletion
=======
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682

from mezzanine.conf import settings

class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_updated', models.DateTimeField(null=True, verbose_name='Last updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', cartridge.shop.fields.SKUField(max_length=20, verbose_name='SKU')),
                ('description', models.CharField(max_length=2000, verbose_name='Description')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('unit_price', cartridge.shop.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10, blank=True, null=True, verbose_name='Unit price')),
                ('total_price', cartridge.shop.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10, blank=True, null=True, verbose_name='Total price')),
                ('url', models.CharField(max_length=2000)),
                ('image', models.CharField(max_length=200, null=True)),
<<<<<<< HEAD
                ('cart', models.ForeignKey(related_name='items', to='shop.Cart', on_delete=django.db.models.deletion.CASCADE)),
=======
                ('cart', models.ForeignKey(related_name='items', to='shop.Cart')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
<<<<<<< HEAD
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page', on_delete=django.db.models.deletion.CASCADE)),
=======
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='pages.Page')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('featured_image', mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Featured Image', blank=True)),
                ('price_min', cartridge.shop.fields.MoneyField(null=True, verbose_name='Minimum price', max_digits=10, decimal_places=2, blank=True)),
                ('price_max', cartridge.shop.fields.MoneyField(null=True, verbose_name='Maximum price', max_digits=10, decimal_places=2, blank=True)),
                ('combined', models.BooleanField(default=True, help_text='If checked, products must match all specified filters, otherwise products can match any specified filter.', verbose_name='Combined')),
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Product category',
                'verbose_name_plural': 'Product categories',
            },
            bases=('pages.page', models.Model),
        ),
        migrations.CreateModel(
            name='DiscountCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('discount_deduct', cartridge.shop.fields.MoneyField(null=True, verbose_name='Reduce by amount', max_digits=10, decimal_places=2, blank=True)),
                ('discount_percent', cartridge.shop.fields.PercentageField(null=True, verbose_name='Reduce by percent', max_digits=5, decimal_places=2, blank=True)),
                ('discount_exact', cartridge.shop.fields.MoneyField(null=True, verbose_name='Reduce to amount', max_digits=10, decimal_places=2, blank=True)),
                ('valid_from', models.DateTimeField(null=True, verbose_name='Valid from', blank=True)),
                ('valid_to', models.DateTimeField(null=True, verbose_name='Valid to', blank=True)),
                ('code', cartridge.shop.fields.DiscountCodeField(unique=True, max_length=20, verbose_name='Code')),
                ('min_purchase', cartridge.shop.fields.MoneyField(null=True, verbose_name='Minimum total purchase', max_digits=10, decimal_places=2, blank=True)),
                ('free_shipping', models.BooleanField(default=False, verbose_name='Free shipping')),
                ('uses_remaining', models.IntegerField(help_text='If you wish to limit the number of times a code may be used, set this value. It will be decremented upon each use.', null=True, verbose_name='Uses remaining', blank=True)),
                ('categories', models.ManyToManyField(related_name='discountcode_related', verbose_name='Categories', to='shop.Category', blank=True)),
            ],
            options={
                'verbose_name': 'Discount code',
                'verbose_name_plural': 'Discount codes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('billing_detail_first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('billing_detail_last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('billing_detail_street', models.CharField(max_length=100, verbose_name='Street')),
                ('billing_detail_city', models.CharField(max_length=100, verbose_name='City/Suburb')),
                ('billing_detail_state', models.CharField(max_length=100, verbose_name='State/Region')),
                ('billing_detail_postcode', models.CharField(max_length=10, verbose_name='Zip/Postcode')),
                ('billing_detail_country', models.CharField(max_length=100, verbose_name='Country')),
                ('billing_detail_phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('billing_detail_email', models.EmailField(max_length=75, verbose_name='Email')),
                ('shipping_detail_first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('shipping_detail_last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('shipping_detail_street', models.CharField(max_length=100, verbose_name='Street')),
                ('shipping_detail_city', models.CharField(max_length=100, verbose_name='City/Suburb')),
                ('shipping_detail_state', models.CharField(max_length=100, verbose_name='State/Region')),
                ('shipping_detail_postcode', models.CharField(max_length=10, verbose_name='Zip/Postcode')),
                ('shipping_detail_country', models.CharField(max_length=100, verbose_name='Country')),
                ('shipping_detail_phone', models.CharField(max_length=20, verbose_name='Phone')),
                ('additional_instructions', models.TextField(verbose_name='Additional instructions', blank=True)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Time', null=True)),
                ('key', models.CharField(max_length=40)),
                ('user_id', models.IntegerField(null=True, blank=True)),
                ('shipping_type', models.CharField(max_length=50, verbose_name='Shipping type', blank=True)),
                ('shipping_total', cartridge.shop.fields.MoneyField(null=True, verbose_name='Shipping total', max_digits=10, decimal_places=2, blank=True)),
                ('tax_type', models.CharField(max_length=50, verbose_name='Tax type', blank=True)),
                ('tax_total', cartridge.shop.fields.MoneyField(null=True, verbose_name='Tax total', max_digits=10, decimal_places=2, blank=True)),
                ('item_total', cartridge.shop.fields.MoneyField(null=True, verbose_name='Item total', max_digits=10, decimal_places=2, blank=True)),
                ('discount_code', cartridge.shop.fields.DiscountCodeField(max_length=20, verbose_name='Discount code', blank=True)),
                ('discount_total', cartridge.shop.fields.MoneyField(null=True, verbose_name='Discount total', max_digits=10, decimal_places=2, blank=True)),
                ('total', cartridge.shop.fields.MoneyField(null=True, verbose_name='Order total', max_digits=10, decimal_places=2, blank=True)),
                ('transaction_id', models.CharField(max_length=255, null=True, verbose_name='Transaction ID', blank=True)),
                ('status', models.IntegerField(default=settings.SHOP_ORDER_STATUS_CHOICES[0][0], verbose_name='Status', choices=settings.SHOP_ORDER_STATUS_CHOICES)),
<<<<<<< HEAD
                ('site', models.ForeignKey(editable=False, to='sites.Site',on_delete=django.db.models.deletion.SET_NULL)),
=======
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            ],
            options={
                'ordering': ('-id',),
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sku', cartridge.shop.fields.SKUField(max_length=20, verbose_name='SKU')),
                ('description', models.CharField(max_length=2000, verbose_name='Description')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('unit_price', cartridge.shop.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10, blank=True, null=True, verbose_name='Unit price')),
                ('total_price', cartridge.shop.fields.MoneyField(decimal_places=2, default=Decimal('0'), max_digits=10, blank=True, null=True, verbose_name='Total price')),
<<<<<<< HEAD
                ('order', models.ForeignKey(related_name='items', to='shop.Order', on_delete=django.db.models.deletion.CASCADE)),
=======
                ('order', models.ForeignKey(related_name='items', to='shop.Order')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keywords_string', models.CharField(max_length=500, editable=False, blank=True)),
                ('rating_count', models.IntegerField(default=0, editable=False)),
                ('rating_sum', models.IntegerField(default=0, editable=False)),
                ('rating_average', models.FloatField(default=0, editable=False)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('_meta_title', models.CharField(help_text='Optional title to be used in the HTML title tag. If left blank, the main title field will be used.', max_length=500, null=True, verbose_name='Title', blank=True)),
                ('description', models.TextField(verbose_name='Description', blank=True)),
                ('gen_description', models.BooleanField(default=True, help_text='If checked, the description will be automatically generated from content. Uncheck if you want to manually set a custom description.', verbose_name='Generate description')),
                ('created', models.DateTimeField(null=True, editable=False)),
                ('updated', models.DateTimeField(null=True, editable=False)),
                ('status', models.IntegerField(default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status', choices=[(1, 'Draft'), (2, 'Published')])),
                ('publish_date', models.DateTimeField(help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from', blank=True)),
                ('expiry_date', models.DateTimeField(help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on', blank=True)),
                ('short_url', models.URLField(null=True, blank=True)),
                ('in_sitemap', models.BooleanField(default=True, verbose_name='Show in sitemap')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('unit_price', cartridge.shop.fields.MoneyField(null=True, verbose_name='Unit price', max_digits=10, decimal_places=2, blank=True)),
                ('sale_id', models.IntegerField(null=True)),
                ('sale_price', cartridge.shop.fields.MoneyField(null=True, verbose_name='Sale price', max_digits=10, decimal_places=2, blank=True)),
                ('sale_from', models.DateTimeField(null=True, verbose_name='Sale start', blank=True)),
                ('sale_to', models.DateTimeField(null=True, verbose_name='Sale end', blank=True)),
                ('sku', cartridge.shop.fields.SKUField(max_length=20, unique=True, null=True, verbose_name='SKU', blank=True)),
                ('num_in_stock', models.IntegerField(null=True, verbose_name='Number in stock', blank=True)),
                ('available', models.BooleanField(default=False, verbose_name='Available for purchase')),
                ('image', models.CharField(max_length=100, null=True, verbose_name='Image', blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='Date added', null=True)),
                ('categories', models.ManyToManyField(to='shop.Category', verbose_name='Product categories', blank=True)),
                ('related_products', models.ManyToManyField(related_name='related_products_rel_+', verbose_name='Related products', to='shop.Product', blank=True)),
<<<<<<< HEAD
                ('site', models.ForeignKey(editable=False, to='sites.Site', on_delete=django.db.models.deletion.SET_NULL)),
=======
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
                ('upsell_products', models.ManyToManyField(related_name='upsell_products_rel_+', verbose_name='Upsell products', to='shop.Product', blank=True)),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
            bases=(models.Model, mezzanine.utils.models.AdminThumbMixin),
        ),
        migrations.CreateModel(
            name='ProductAction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.IntegerField()),
                ('total_cart', models.IntegerField(default=0)),
                ('total_purchase', models.IntegerField(default=0)),
<<<<<<< HEAD
                ('product', models.ForeignKey(related_name='actions', to='shop.Product', on_delete=django.db.models.deletion.CASCADE)),
=======
                ('product', models.ForeignKey(related_name='actions', to='shop.Product')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_order', models.IntegerField(null=True, verbose_name='Order')),
                ('file', models.ImageField(upload_to='product', verbose_name='Image')),
                ('description', models.CharField(max_length=100, verbose_name='Description', blank=True)),
<<<<<<< HEAD
                ('product', models.ForeignKey(related_name='images', to='shop.Product',on_delete=django.db.models.deletion.CASCADE)),
=======
                ('product', models.ForeignKey(related_name='images', to='shop.Product')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            ],
            options={
                'ordering': ('_order',),
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(verbose_name='Type', choices=[(1, 'Size'), (2, 'Colour')])),
                ('name', cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Product option',
                'verbose_name_plural': 'Product options',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProductVariation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('unit_price', cartridge.shop.fields.MoneyField(null=True, verbose_name='Unit price', max_digits=10, decimal_places=2, blank=True)),
                ('sale_id', models.IntegerField(null=True)),
                ('sale_price', cartridge.shop.fields.MoneyField(null=True, verbose_name='Sale price', max_digits=10, decimal_places=2, blank=True)),
                ('sale_from', models.DateTimeField(null=True, verbose_name='Sale start', blank=True)),
                ('sale_to', models.DateTimeField(null=True, verbose_name='Sale end', blank=True)),
                ('sku', cartridge.shop.fields.SKUField(max_length=20, unique=True, null=True, verbose_name='SKU', blank=True)),
                ('num_in_stock', models.IntegerField(null=True, verbose_name='Number in stock', blank=True)),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('option1', cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Size')),
                ('option2', cartridge.shop.fields.OptionField(max_length=50, null=True, verbose_name='Colour')),
<<<<<<< HEAD
                ('image', models.ForeignKey(verbose_name='Image', blank=True, to='shop.ProductImage', null=True, on_delete=django.db.models.deletion.SET_NULL)),
                ('product', models.ForeignKey(related_name='variations', to='shop.Product', on_delete=django.db.models.deletion.SET_NULL)),
=======
                ('image', models.ForeignKey(verbose_name='Image', blank=True, to='shop.ProductImage', null=True)),
                ('product', models.ForeignKey(related_name='variations', to='shop.Product')),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            ],
            options={
                'ordering': ('-default',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('active', models.BooleanField(default=False, verbose_name='Active')),
                ('discount_deduct', cartridge.shop.fields.MoneyField(null=True, verbose_name='Reduce by amount', max_digits=10, decimal_places=2, blank=True)),
                ('discount_percent', cartridge.shop.fields.PercentageField(null=True, verbose_name='Reduce by percent', max_digits=5, decimal_places=2, blank=True)),
                ('discount_exact', cartridge.shop.fields.MoneyField(null=True, verbose_name='Reduce to amount', max_digits=10, decimal_places=2, blank=True)),
                ('valid_from', models.DateTimeField(null=True, verbose_name='Valid from', blank=True)),
                ('valid_to', models.DateTimeField(null=True, verbose_name='Valid to', blank=True)),
                ('categories', models.ManyToManyField(related_name='sale_related', verbose_name='Categories', to='shop.Category', blank=True)),
                ('products', models.ManyToManyField(to='shop.Product', verbose_name='Products', blank=True)),
            ],
            options={
                'verbose_name': 'Sale',
                'verbose_name_plural': 'Sales',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='productaction',
            unique_together=set([('product', 'timestamp')]),
        ),
        migrations.AddField(
            model_name='discountcode',
            name='products',
            field=models.ManyToManyField(to='shop.Product', verbose_name='Products', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='options',
            field=models.ManyToManyField(related_name='product_options', verbose_name='Product options', to='shop.ProductOption', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(to='shop.Product', verbose_name='Products', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='category',
            name='sale',
<<<<<<< HEAD
            field=models.ForeignKey(verbose_name='Sale', blank=True, to='shop.Sale', null=True, on_delete=django.db.models.deletion.SET_NULL),
=======
            field=models.ForeignKey(verbose_name='Sale', blank=True, to='shop.Sale', null=True),
>>>>>>> 711f42ce68f843f511bec16f048afce519b0f682
            preserve_default=True,
        ),
    ]
