#pragma once

#include "dart/dart.hpp"
#include "Character.h"
#include "ReferenceManager.h"

namespace ICC
{

enum class TerminationReason{
	NOT_TERMINATED,
	ROOT_HEIGHT,
	ROOT_DIFF,
	ROOT_ANGLE_DIFF,
	OUT_OF_AREA,
	NAN_P,
	NAN_V,
	END_OF_TRAJECTORY,
};

/**
*
* @brief Environment class
* @details execute forward dynamics simulations
* 
*/
class Environment
{
public:
	/// Constructor
	Environment();

	/// Step environment
	void step();

	/// Reset environment
	void reset(double reset_time = 0);

	/// Get state
	Eigen::VectorXd getState();

	/// Get end effector state from joint p, v
	Eigen::VectorXd getEndEffectorStatePV(const dart::dynamics::SkeletonPtr skel, const Eigen::VectorXd& pv);

	/// Set action
	void setAction(const Eigen::VectorXd& action);

	/// Get reward
	std::vector<double> getReward();

	/// Check whether the episode is terminated or not
	bool isTerminal();
	/// Check whether the episode is temrinated by nan or not
	bool isNanAtTerminal(){
		return this->mIsNanAtTerminal;
	}
	/// Check whether the episode is temrinated by end of trajectory or not
	bool isEndOfTrajectory(){
		return this->mTerminationReason == TerminationReason::END_OF_TRAJECTORY;
	}

	/// Get the size of the state
	int getStateSize(){ return this->mStateSize; }
	/// Get the size of the action
	int getActionSize(){ return this->mActionSize; }

	/// Get dart world pointer
	const dart::simulation::WorldPtr& getWorld(){ return this->mWorld; }

	/// Set reference trajectory
	void setReferenceTrajectory(Eigen::MatrixXd trajectory);

	std::vector<Eigen::VectorXd> getPositionsForMG();
protected:
	dart::simulation::WorldPtr mWorld;

	Character* mActor;
	Character* mGround;
	ReferenceManager* mReferenceManager;

	int mStateSize, mActionSize;

	int mControlHz, mSimulationHz;

	/// End-effector list
	std::vector<std::string> mEndEffectors;

	// Joints used in reward evaluation
	std::vector<std::string> mRewardJoints;

	Eigen::VectorXd mAction;

	bool mIsTerminal;
	bool mIsNanAtTerminal;
	TerminationReason mTerminationReason;

	Eigen::VectorXd mTargetPositions, mTargetVelocities;
	Eigen::VectorXd mModifiedTargetPositions, mModifiedTargetVelocities;

};

}