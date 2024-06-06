from django import forms
from . import models
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from userauths.models import User



# class ProfileForm(forms.ModelForm):
#   class meta:
#     model = models.profile
#     fields =['image','country','address']



class UserCreationForms(UserCreationForm):
  countries = [
      ('AZ', 'أذربيجان'),
      ('AM', 'أرمينيا'),
      ('AW', 'أروبا'),
      ('AU', 'أستراليا'),
      ('AF', 'أفغانستان'),
      ('AL', 'ألبانيا'),
      ('DE', 'ألمانيا'),
      ('AG', 'أنتيغوا وبربودا'),
      ('AD', 'أندورا'),
      ('AO', 'أنغولا'),
      ('UZ', 'أوزبكستان'),
      ('UG', 'أوغندا'),
      ('UA', 'أوكرانيا'),
      ('IE', 'أيرلندا'),
      ('IS', 'أيسلندا'),
      ('ET', 'إثيوبيا'),
      ('ER', 'إريتريا'),
      ('ES', 'إسبانيا'),
      ('EE', 'إستونيا'),
      ('IL', 'إسرائيل'),
      ('ID', 'إندونيسيا'),
      ('IR', 'إيران'),
      ('IT', 'إيطاليا'),
      ('AR', 'الأرجنتين'),
      ('JO', 'الأردن'),
      ('EC', 'الإكوادور'),
      ('AE', 'الإمارات العربية المتحدة'),
      ('BH', 'البحرين'),
      ('BR', 'البرازيل'),
      ('PT', 'البرتغال'),
      ('BA', 'البوسنة والهرسك'),
      ('ME', 'الجبل الأسود'),
      ('DZ', 'الجزائر'),
      ('DK', 'الدنمارك'),
      ('CV', 'الرأس الأخضر'),
      ('SA', 'السعودية'),
      ('SV', 'السلفادور'),
      ('SN', 'السنغال'),
      ('SD', 'السودان'),
      ('SE', 'السويد'),
      ('SO', 'الصومال'),
      ('CN', 'الصين'),
      ('IQ', 'العراق'),
      ('VA', 'الفاتيكان'),
      ('PH', 'الفلبين'),
      ('CM', 'الكاميرون'),
      ('KW', 'الكويت'),
      ('HU', 'المجر'),
      ('MA', 'المغرب'),
      ('MX', 'المكسيك'),
      ('GB', 'المملكة المتحدة'),
      ('NO', 'النرويج'),
      ('AT', 'النمسا'),
      ('NE', 'النيجر'),
      ('IN', 'الهند'),
      ('US', 'الولايات المتحدة الأمريكية'),
      ('JP', 'اليابان'),
      ('YE', 'اليمن'),
      ('GR', 'اليونان'),
      ('PG', 'بابوا غينيا الجديدة'),
      ('PY', 'باراغواي'),
      ('PK', 'باكستان'),
      ('PW', 'بالاو'),
      ('BB', 'بربادوس'),
      ('BN', 'بروناي'),
      ('BE', 'بلجيكا'),
      ('BG', 'بلغاريا'),
      ('BD', 'بنغلاديش'),
      ('PA', 'بنما'),
      ('BJ', 'بنين'),
      ('BT', 'بوتان'),
      ('BW', 'بوتسوانا'),
      ('BF', 'بوركينا فاسو'),
      ('BI', 'بوروندي'),
      ('PL', 'بولندا'),
      ('BO', 'بوليفيا'),
      ('PE', 'بيرو'),
      ('TH', 'تايلاند'),
      ('TW', 'تايوان'),
      ('TM', 'تركمانستان'),
      ('TR', 'تركيا'),
      ('TT', 'ترينيداد وتوباغو'),
      ('TD', 'تشاد'),
      ('CL', 'تشيلي'),
      ('TZ', 'تنزانيا'),
      ('TG', 'توغو'),
      ('TV', 'توفالو'),
      ('TN', 'تونس'),
      ('TL', 'تيمور الشرقية'),
      ('JM', 'جامايكا'),
      ('BS', 'جزر البهاما'),
      ('KM', 'جزر القمر'),
      ('MV', 'جزر المالديف'),
      ('MH', 'جزر مارشال'),
      ('SB', 'جزر سليمان'),
      ('FO', 'جزر فارو'),
      ('FJ', 'جزر فيجي'),
      ('KY', 'جزر كايمان'),
      ('CK', 'جزر كوك'),
      ('MP', 'جزر ماريانا الشمالية'),
      ('CF', 'جمهورية أفريقيا الوسطى'),
      ('CZ', 'جمهورية التشيك'),
      ('DO', 'جمهورية الدومينيكان'),
      ('CD', 'جمهورية الكونغو الديمقراطية'),
      ('CG', 'جمهورية الكونغو'),
      ('MK', 'جمهورية مقدونيا'),
      ('ZA', 'جنوب أفريقيا'),
      ('SS', 'جنوب السودان'),
      ('GT', 'جواتيمالا'),
      ('GE', 'جورجيا'),
      ('DJ', 'جيبوتي'),
      ('DM', 'دومينيكا'),
      ('RW', 'رواندا'),
      ('RU', 'روسيا'),
      ('RO', 'رومانيا'),
      ('ZM', 'زامبيا'),
      ('ZW', 'زيمبابوي'),
      ('CI', 'ساحل العاج'),
      ('WS', 'ساموا'),
      ('SM', 'سان مارينو'),
      ('VC', 'سانت فينسنت والغرينادين'),
      ('KN', 'سانت كيتس ونيفيس'),
      ('LC', 'سانت لوسيا'),
      ('ST', 'ساو تومي وبرينسيب'),
      ('LK', 'سريلانكا'),
      ('SK', 'سلوفاكيا'),
      ('SI', 'سلوفينيا'),
      ('SG', 'سنغافورة'),
      ('SZ', 'سوازيلاند'),
      ('SY', 'سوريا'),
      ('SR', 'سورينام'),
      ('CH', 'سويسرا'),
      ('SL', 'سيراليون'),
      ('SC', 'سيشل'),
      ('CL', 'شيلي'),
      ('RS', 'صربيا'),
      ('TJ', 'طاجيكستان'),
      ('OM', 'عمان'),
      ('GM', 'غامبيا'),
      ('GH', 'غانا'),
      ('GD', 'غرينادا'),
      ('GT', 'غواتيمالا'),
      ('GY', 'غويانا'),
      ('GF', 'غيانا الفرنسية'),
      ('GN', 'غينيا'),
      ('GQ', 'غينيا الاستوائية'),
      ('GW', 'غينيا بيساو'),
      ('VU', 'فانواتو'),
      ('FR', 'فرنسا'),
      ('PS', 'فلسطين'),
      ('VE', 'فنزويلا'),
      ('FI', 'فنلندا'),
      ('VN', 'فيتنام'),
      ('CY', 'قبرص'),
      ('KG', 'قرغيزستان'),
      ('QA', 'قطر'),
      ('KZ', 'كازاخستان'),
      ('NC', 'كاليدونيا الجديدة'),
      ('HR', 'كرواتيا'),
      ('KH', 'كمبوديا'),
      ('CA', 'كندا'),
      ('CU', 'كوبا'),
      ('KR', 'كوريا الجنوبية'),
      ('KP', 'كوريا الشمالية'),
      ('CO', 'كولومبيا'),
      ('CR', 'كوستاريكا'),
      ('KI', 'كيريباتي'),
      ('KE', 'كينيا'),
      ('LV', 'لاتفيا'),
      ('LA', 'لاوس'),
      ('LB', 'لبنان'),
      ('LU', 'لوكسمبورغ'),
      ('LY', 'ليبيا'),
      ('LR', 'ليبيريا'),
      ('LT', 'ليتوانيا'),
      ('LI', 'ليختنشتاين'),
      ('LS', 'ليسوتو'),
      ('MT', 'مالطا'),
      ('ML', 'مالي'),
      ('MY', 'ماليزيا'),
      ('MG', 'مدغشقر'),
      ('EG', 'مصر'),
      ('MW', 'ملاوي'),
      ('MN', 'منغوليا'),
      ('MR', 'موريتانيا'),
      ('MU', 'موريشيوس'),
      ('MZ', 'موزمبيق'),
      ('MD', 'مولدوفا'),
      ('MC', 'موناكو'),
  ]

  email =  forms.EmailField(required=True,widget=forms.EmailInput(attrs={"placeholder":"Enter Your Email","class":"form-control","autofocus":"True"}))
  username =  forms.CharField(required=True,widget=forms.TextInput(attrs={"placeholder":"Enter username","class":"form-control","autofocus":"False","target":"_blank"}),label='اسم المستخدم: ')
  phone =  forms.CharField(required=True,widget=forms.TimeInput(attrs={"placeholder":"Enter Phone","class":"form-control","type":"tel"}))
  country = forms.ChoiceField(required=True,widget=forms.Select(attrs={"class":"form-control selectpicker","data-live-search":"true","title":"أختر البلد ..."}),label='البلد:', choices=countries)
  password1 = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"كلمة المرور", "id":"password"}),min_length=8)
  password2= forms.CharField( widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"تأكيد كلمة المرور", "id":"password"}),min_length=8)
  class Meta:
    model = User
    fields = ('username','email', 'phone','country', 'password1','password2')



class Login_Form(forms.ModelForm):
    email = forms.CharField(label='البريد الإلكتروني')
    password = forms.CharField(label='كلمة المرور', widget=forms.PasswordInput())
    class Meta:
      model = User
      fields = ('username' , 'password' , 'email')


class UpdateUserForm(forms.ModelForm):
    first_name =  forms.CharField(label='الإسم الأول: ')
    last_name =  forms.CharField(label='الإسم الأخير: ')
    email =  forms.EmailField(label=' البريد الإلكتروني: ')
    class Meta:
      model = User
      fields = ('first_name' , 'last_name', 'email')



class AvailabilityForm(forms.Form):
  Room_Type = [
    ('S', 'غرفة لفرد واحد'),
    ('D', 'غرفة لفردين'),
    ('M', 'غرفة لفردين أو أكثر'),
    ('F', 'غرفة لعائلة'),
  ]
  room_type = forms.ChoiceField(choices=Room_Type,required=True)
  arrival_date =forms.DateTimeField(required=True,input_formats=["%Y-%m-%dt%H:%M", ])
  leave_date =forms.DateTimeField(required=True,input_formats=["%Y-%m-%dt%H:%M", ])