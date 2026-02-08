import { motion } from 'framer-motion';
import { CheckCircleIcon, XCircleIcon, PencilIcon, TrashIcon } from '@heroicons/react/24/outline';

export default function TaskCard({ task, onToggleStatus, onDelete, onEdit }) {
  const priorityColors = {
    high: 'bg-red-100 text-red-800',
    medium: 'bg-yellow-100 text-yellow-800',
    low: 'bg-green-100 text-green-800'
  };

  return (
    <motion.div
      layout
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className={`bg-white rounded-xl shadow-md p-6 flex flex-col md:flex-row md:items-center justify-between ${task.status === 'completed' ? 'opacity-75' : ''}`}
    >
      <div className="flex items-start space-x-4 flex-1 mb-4 md:mb-0">
        <button
          onClick={() => onToggleStatus(task.id)}
          className={`mt-1 flex-shrink-0 h-6 w-6 rounded-full border-2 flex items-center justify-center ${
            task.status === 'completed' 
              ? 'bg-green-500 border-green-500 text-white' 
              : 'border-gray-300 hover:border-indigo-500'
          }`}
        >
          {task.status === 'completed' && <CheckCircleIcon className="h-4 w-4" />}
        </button>
        
        <div className="flex-1">
          <div className="flex flex-wrap items-center gap-2 mb-1">
            <h3 className={`font-semibold ${task.status === 'completed' ? 'line-through text-gray-500' : 'text-gray-800'}`}>
              {task.title}
            </h3>
            <span className={`text-xs px-2 py-1 rounded-full ${priorityColors[task.priority]}`}>
              {task.priority.charAt(0).toUpperCase() + task.priority.slice(1)}
            </span>
            {task.dueDate && (
              <span className="text-xs bg-blue-100 text-blue-800 px-2 py-1 rounded-full">
                Due: {new Date(task.dueDate).toLocaleDateString()}
              </span>
            )}
          </div>
          
          {task.description && (
            <p className={`text-gray-600 mt-1 ${task.status === 'completed' ? 'line-through' : ''}`}>
              {task.description}
            </p>
          )}
        </div>
      </div>
      
      <div className="flex space-x-2">
        <button
          onClick={() => onEdit(task)}
          className="p-2 text-gray-500 hover:text-indigo-600 hover:bg-indigo-50 rounded-full"
        >
          <PencilIcon className="h-5 w-5" />
        </button>
        <button
          onClick={() => onDelete(task.id)}
          className="p-2 text-gray-500 hover:text-red-600 hover:bg-red-50 rounded-full"
        >
          <TrashIcon className="h-5 w-5" />
        </button>
      </div>
    </motion.div>
  );
}