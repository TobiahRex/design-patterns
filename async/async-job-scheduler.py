import asyncio
from typing import Callable, Any

class JobScheduler:
    def __init__(self):
        self.queue = asyncio.Queue()

    def schedule(self, job: Callable[[], Any]) -> None:
        """Schedules a new job to be run."""
        asyncio.create_task(self.queue.put(job))

    async def run(self) -> None:
        """Runs the scheduler loop, which waits for jobs to be scheduled and runs them."""
        while True:
            # Wait for a job to be scheduled
            job = await self.queue.get()
            # Run the job
            await job()
            # Mark the job as done
            self.queue.task_done()

# Create an instance of the JobScheduler class
scheduler = JobScheduler()

# Schedule a job
scheduler.schedule(lambda: print('Hello, World!'))

# Start the scheduler loop
asyncio.run(scheduler.run())
