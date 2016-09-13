from django.db import models
from processMap.models import ProcessStep
from certification.models import RequiredCertificationDocuments

class HFCContaminantsRiskMap(models.Model):
    document = models.OneToOneField(RequiredCertificationDocuments, on_delete=models.PROTECT)

    def __str__(self):
        return self.document

class InvolvedRisk(models.Model):
    risk_map = models.ForeignKey(HFCContaminantsRiskMap, on_delete=models.PROTECT)
    process_step = models.ForeignKey(ProcessStep, on_delete=models.PROTECT)
    involved_risk = models.CharField(max_length=50, default='')
    control_method = models.CharField(max_length=50, default='')
    preventive_action = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.involved_risk