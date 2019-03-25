from .models import Contracts
from django.shortcuts import get_object_or_404


def last_rank(seaman_id):
    """Возвращает должность по последнему/текущему контракту
    """
    contracts = Contracts.objects.filter(seaman=seaman_id).all()
    dates = []
    for contract in contracts:
        dates.append(contract.sign_in_date)
    contract = get_object_or_404(Contracts, sign_in_date=max(dates))

    return contract.rank
