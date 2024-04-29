from .models import UserPreferences

def get_currency (request) :
    
    if request.user.is_authenticated :
        data = UserPreferences.objects.filter(user=request.user).last()
        return {'currency':data}
    else :
        return{}