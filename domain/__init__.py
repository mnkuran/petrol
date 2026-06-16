from protean import Domain


domain = Domain()
domain.config["event_processing"] = "sync"
domain.config["command_processing"] = "sync"
domain.init()