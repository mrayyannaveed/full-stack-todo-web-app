import { motion } from 'framer-motion';

export default function StatsBar({ totalTasks, completedTasks, pendingTasks }) {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.1 }}
      className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8"
    >
      <div className="bg-white rounded-xl shadow-md p-6 text-center">
        <h3 className="text-2xl font-bold text-gray-800">{totalTasks}</h3>
        <p className="text-gray-600">Total Tasks</p>
      </div>
      <div className="bg-white rounded-xl shadow-md p-6 text-center">
        <h3 className="text-2xl font-bold text-green-600">{completedTasks}</h3>
        <p className="text-gray-600">Completed</p>
      </div>
      <div className="bg-white rounded-xl shadow-md p-6 text-center">
        <h3 className="text-2xl font-bold text-yellow-600">{pendingTasks}</h3>
        <p className="text-gray-600">Pending</p>
      </div>
    </motion.div>
  );
}