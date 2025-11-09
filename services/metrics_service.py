from services.db_service import DBService
import inspect
import pkgutil
import importlib
import os

class MetricsService:
    def __init__(self):
        self.db = DBService()

    def get_parking_history(self):
        return self.db.get_all_history()

    def calculate_system_metrics(self):
        """Basic object-oriented and runtime metrics."""
        metrics = {
            "Total Classes": 0,
            "Total Methods": 0,
            "Total Attributes": 0,
            "Inheritance Relations": 0,
            "Total Vehicles Parked": len(self.db.get_all_history()),
            "Total Revenue": sum(row[7] for row in self.db.get_all_history()),
        }

        package_path = os.path.join(os.getcwd(), "models")
        for _, module_name, _ in pkgutil.iter_modules([package_path]):
            module = importlib.import_module(f"models.{module_name}")
            for name, obj in inspect.getmembers(module, inspect.isclass):
                metrics["Total Classes"] += 1
                metrics["Total Methods"] += len(inspect.getmembers(obj, inspect.isfunction))
                metrics["Total Attributes"] += len(obj.__dict__.keys())
                if obj.__bases__ and obj.__bases__[0].__name__ != 'object':
                    metrics["Inheritance Relations"] += 1

        return metrics
